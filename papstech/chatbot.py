# Simple chatbot implementation
def chatbot():
	print("Hi! 👋 I'm Paps Technologies Bot. Type 'bye' anytime to end our chat. How can I help you today?")
	while True:
		user_input = input("You: ").strip().lower()
		if user_input == 'bye':
			print("Paps Technologies Bot: Goodbye! It was nice chatting with you. If you have more questions, just come back anytime!")
			break
		elif user_input in ['hi', 'hii', 'hello']:
			print("Paps Technologies Bot: Hey there! 😊 How can I assist you today? You can ask me about our services, company info, or anything else!")
		elif 'how are you' in user_input:
			print("Paps Technologies Bot: I'm doing great, thanks for asking! How are you today?")
		elif 'name' in user_input:
			print("Paps Technologies Bot: My name is Paps Technologies Bot, but you can call me Paps! 😊 What's your name?")
		elif 'founder' in user_input:
			print("Paps Technologies Bot: Our founder is Saravanan. Would you like to know more about our team?")
		elif 'co founder' in user_input or 'co-founder' in user_input:
			print("Paps Technologies Bot: The co-founder of Paps Technologies is Naveen. He's part of our passionate team working for your success!")
		elif 'paps technologies' in user_input or 'company' in user_input:
			print("Paps Technologies Bot: Paps Technologies is a digital marketing agency based in Chennai, India. We help businesses grow online with web design, SEO, social media, and more. Want to know how we can help you?")
		elif 'services' in user_input:
			print("Paps Technologies Bot: We offer web design, SEO, SEM, social media marketing, mobile app development, local SEO, content marketing, and brand identity. Which service interests you most?")
		elif 'contact' in user_input or 'phone' in user_input or 'email' in user_input:
			print("Paps Technologies Bot: You can reach us at +91-824-880-8145 or papstechnologies@gmail.com. We're located in Salem, Chennai, Tamil Nadu. Would you like directions or a callback?")
		elif 'industries' in user_input:
			print("Paps Technologies Bot: We work with finance, healthcare, restaurants, fitness, events, FMCG, interior, translation, IT, cosmetics, and more. Is your business in one of these industries?")
		elif 'location' in user_input:
			print("Paps Technologies Bot: We're located in Salem, Chennai, Tamil Nadu, India. We also work with clients across India and abroad!")
		elif 'hours' in user_input or 'timing' in user_input:
			print("Paps Technologies Bot: We're open Monday to Saturday, 9:30 AM to 6:30 PM. When would you like to visit or call?")
		else:
			print("Paps Technologies Bot: I'm not sure about that yet, but I'm always learning! Can I help you with something about Paps Technologies, digital marketing, or business growth?")

if __name__ == "__main__":
	chatbot()

