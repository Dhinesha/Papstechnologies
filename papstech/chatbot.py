# Simple chatbot implementation
def chatbot():
	print("Hello! I am Paps Technologies Bot. Type 'bye' to exit.")
	while True:
		user_input = input("You: ").strip().lower()
		if user_input == 'bye':
			print("Paps Technologies Bot: Goodbye!")
			break
		elif user_input in ['hi', 'hii', 'hello']:
			print("Paps Technologies Bot: Hey there! 😊 I'm Paps Technologies Bot. How can I help you today? Feel free to ask me anything about our services or company.")
		elif 'how are you' in user_input:
			print("Paps Technologies Bot: I'm great, thanks for asking! How are you doing?")
		elif 'name' in user_input:
			print("Paps Technologies Bot: My name is Paps Technologies Bot, but you can call me Paps! 😊")
		elif 'founder' in user_input:
			print("Paps Technologies Bot: The founder of Paps Technologies is Saravanan.")
		elif 'co founder' in user_input or 'co-founder' in user_input:
			print("Paps Technologies Bot: The co-founder of Paps Technologies is Naveen.")
		elif 'paps technologies' in user_input or 'company' in user_input:
			print("Paps Technologies Bot: Paps Technologies is a digital marketing agency in Chennai, India. We offer web design, SEO, SEM, SMM, mobile app development, and more.")
		elif 'services' in user_input:
			print("Paps Technologies Bot: Our services include Web Design & Development, SEO, SEM, Social Media Marketing, Mobile App Development, Local SEO, Content Marketing, and Brand Identity.")
		elif 'contact' in user_input or 'phone' in user_input or 'email' in user_input:
			print("Paps Technologies Bot: You can contact Paps Technologies at +91-824-880-8145 or papstechnologies@gmail.com. We are located in Salem, Chennai, Tamil Nadu.")
		elif 'industries' in user_input:
			print("Paps Technologies Bot: We serve Finance, Healthcare, Restaurants, Fitness, Events, FMCG, Interior, Translation, IT, and Cosmetics industries.")
		elif 'location' in user_input:
			print("Paps Technologies Bot: Paps Technologies is located in Salem, Chennai, Tamil Nadu, India.")
		elif 'hours' in user_input or 'timing' in user_input:
			print("Paps Technologies Bot: We are open Monday to Saturday, 9:30 AM to 6:30 PM.")
		else:
			print("Paps Technologies Bot: Sorry, I'm not aware about that. Can I help you with something related to Paps Technologies?")

if __name__ == "__main__":
	chatbot()
