import google.generativeai as palm

# Directly specify the API key
palm_api_key = "AIzaSyD7CcYRXcznLWaP4LrK0Ghe6tIVhod4j2o"  # Replace with your actual API key

# Create a config
palm.configure(api_key=palm_api_key)
model = palm.GenerativeModel(model_name="gemini-1.5-flash-8b-exp-0924")

# Generate some text
def generate_itinerary(source, destination, start_date, end_date, no_of_day):
    prompt = f"Generate a personalized trip itinerary for a {no_of_day}-day trip from {source} to {destination} on {start_date} to {end_date}, with an optimum budget (Currency:INR)."
    response = model.generate_content(prompt)
    return(response.text)
