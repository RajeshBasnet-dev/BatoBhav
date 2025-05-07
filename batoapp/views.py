from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import PropertyForm
from .models import PredictionHistory, UserFeedback
from price_model.preprocess import preprocess_input
import joblib
import os

def predict_price(request):
    prediction = None
    rental_estimate = None
    market_comparison = None
    city = None
    prediction_id = None

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            city = form.cleaned_data['city']
            input_data = preprocess_input(area, bedrooms, bathrooms, city)
            model_path = os.path.join('price_model', 'model.pkl')
            model = joblib.load(model_path)
            prediction = model.predict(input_data)[0]
            rental_estimate = prediction * 0.005  # Example: 0.5% monthly yield
            # Simplified market comparison (replace with real data if available)
            market_comparison = "Above average" if city == 'Kathmandu' else "Competitive"
            prediction_obj = PredictionHistory.objects.create(
                area=area,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                city=city,
                predicted_price=prediction
            )
            prediction_id = prediction_obj.id
    else:
        form = PropertyForm()
    
    history = PredictionHistory.objects.all().order_by('-created_at')[:5]
    return render(request, 'index.html', {
        'form': form,
        'prediction': prediction,
        'rental_estimate': rental_estimate,
        'market_comparison': market_comparison,
        'city': city,
        'prediction_id': prediction_id,
        'history': history
    })

def submit_feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        prediction_id = request.POST.get('prediction_id')
        UserFeedback.objects.create(
            prediction_id=prediction_id,
            feedback=feedback
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)