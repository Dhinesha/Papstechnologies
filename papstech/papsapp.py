from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Chatbot logic

def get_bot_response(user_input):
    user_input = user_input.strip().lower()
    # Humanized conversational prompts
    if user_input == 'bye':
        return "Goodbye! Have a wonderful day!"
    elif user_input in ['hi', 'hii', 'hello']:
        return "Hi there! 😊 I'm Paps Technologies Bot. How can I assist you today? Feel free to ask me anything about our services or your business needs."
    elif 'what services' in user_input and 'provide' in user_input:
        return "We offer web design, SEO, social media marketing, app development, and online advertising. Would you like more details about any of these?"
    elif 'new website' in user_input and 'business' in user_input:
        return "Absolutely! We build modern, mobile-friendly websites. Are you looking for a simple site or something custom-made for your business?"
    elif 'get more customers' in user_input or ('help' in user_input and 'customers' in user_input):
        return "Definitely! We use SEO, Google Ads, and social media campaigns to help you reach more customers. Would you like me to explain how SEO can help your business grow?"
    elif 'how much' in user_input and 'cost' in user_input:
        return "Our pricing depends on your project and requirements. We offer both budget-friendly and premium plans. Would you like a free quote?"
    elif 'mobile app development' in user_input or ('app' in user_input and 'development' in user_input):
        return "Yes, we create mobile apps with user-friendly design and smooth performance. Do you need an Android app, iOS app, or both?"
    elif 'grow my local business' in user_input or ('local' in user_input and 'business' in user_input):
        return "We specialize in local SEO, Google My Business optimization, and review management to attract nearby customers. Would you like to know how it works?"
    elif 'experience' in user_input and ('healthcare' in user_input or 'retail' in user_input):
        return "Yes, we've worked with healthcare, retail, restaurants, fitness, and many other industries. Would you like to hear some success stories?"
    elif 'track results' in user_input:
        return "We provide detailed reports on website traffic, search rankings, and conversions so you can see your growth. Would you like to see a sample report?"
    elif 'free consultation' in user_input:
        return "Yes, we offer a free initial consultation to understand your needs and suggest the best solutions. Would you like to book a session?"
    elif 'handle my social media' in user_input or ('social media' in user_input and 'pages' in user_input):
        return "Absolutely! We create engaging posts, run ads, and boost your presence on Facebook, Instagram, and other platforms. Which social media do you use most?"
    elif 'how soon' in user_input and 'seo' in user_input:
        return "SEO usually takes 3 to 6 months for strong results, but you'll start seeing improvements earlier. Would you like to combine SEO with paid ads for faster growth?"
    elif 'where are you located' in user_input or ('location' in user_input and 'you' in user_input):
        return "We're based in Salem and Chennai, Tamil Nadu, but we work with clients all over India and abroad. Would you like our contact details?"
    elif 'manage google ads' in user_input or ('google ads' in user_input and 'manage' in user_input):
        return "Yes, we run optimized Google Ads to bring you more leads at a lower cost. Do you have a budget in mind for your ads?"
    elif 'redesign old website' in user_input or ('redesign' in user_input and 'website' in user_input):
        return "Yes, we can redesign your old website with a fresh look and better performance. Would you like to see some examples of our redesigns?"
    elif 'how do i contact' in user_input or ('contact' in user_input and 'how' in user_input):
        return "You can call, email, or fill out our contact form. Would you like me to share our phone number now?"
    # Old prompts, humanized
    elif 'how are you' in user_input:
        return "I'm doing great, thank you for asking! How are you today?"
    elif 'name' in user_input:
        return "My name is Paps Technologies Bot, but you can call me Paps! 😊"
    elif 'founder' in user_input:
        return "Our founder is Saravanan."
    elif 'co founder' in user_input or 'co-founder' in user_input:
        return "Our co-founder is Naveen."
    elif 'paps technologies' in user_input or 'company' in user_input:
        return "Paps Technologies is a digital marketing agency based in Chennai, India. We help businesses grow online with web design, SEO, social media, and more."
    elif 'services' in user_input:
        return "We offer web design, SEO, SEM, social media marketing, mobile app development, local SEO, content marketing, and brand identity services."
    elif 'contact' in user_input or 'phone' in user_input or 'email' in user_input:
        return "You can reach us at +91-824-880-8145 or papstechnologies@gmail.com. We're located in Salem, Chennai, Tamil Nadu."
    elif 'industries' in user_input:
        return "We work with finance, healthcare, restaurants, fitness, events, FMCG, interior, translation, IT, cosmetics, and more."
    elif 'location' in user_input:
        return "We're located in Salem, Chennai, Tamil Nadu, India."
    elif 'hours' in user_input or 'timing' in user_input:
        return "We're open Monday to Saturday, 9:30 AM to 6:30 PM."
    else:
        return "Sorry, I don't have information about that yet. Can I help you with something related to Paps Technologies or digital marketing?"

# HTML template for chat UI
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paps Technologies Bot</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: url('https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1500&q=80') no-repeat center center fixed;
            background-size: cover;
            margin: 0;
        }
        .chatbox {
            width: 400px;
            max-width: 95vw;
            margin: 30px auto;
            background: rgba(20,24,48,0.92);
            border-radius: 16px;
            box-shadow: 0 4px 24px #6d4affcc;
            padding: 24px 10px 20px 10px;
            position: relative;
        }
        @media (max-width: 500px) {
            .chatbox {
                width: 98vw;
                margin: 10px auto;
                padding: 10px 2vw 16px 2vw;
            }
            .messages {
                height: 220px;
                font-size: 0.98em;
            }
            input[type=text] {
                width: 65%;
                font-size: 1em;
            }
            button {
                padding: 8px 12px;
                font-size: 0.98em;
            }
            h2 {
                font-size: 1.2em;
            }
        }
        .robot-icon {
            width: 60px;
            height: 60px;
            display: block;
            margin: 0 auto 10px auto;
        }
        .messages {
            height: 300px;
            overflow-y: auto;
            border: 1px solid #6d4aff;
            padding: 10px;
            margin-bottom: 10px;
            background: rgba(40,44,84,0.95);
            border-radius: 8px;
        }
        .user {
            color: #6dd5fa;
            margin-bottom: 6px;
            text-align: right;
        }
        .bot {
            color: #e0b3ff;
            margin-bottom: 6px;
            text-align: left;
        }
        input[type=text] {
            width: 75%;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #6d4aff;
            font-size: 1em;
            background: #23244a;
            color: #fff;
        }
        button {
            padding: 10px 18px;
            border-radius: 6px;
            border: none;
            background: #6d4aff;
            color: #fff;
            font-size: 1em;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover {
            background: #23244a;
        }
        h2 {
            text-align: center;
            margin-top: 0;
            color: #e0b3ff;
        }
    </style>
</head>
<body>
    <div class="chatbox">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" alt="Robot Icon" class="robot-icon" />
    <h2>Paps Technologies Bot</h2>
    <p style="text-align:center;color:#e0b3ff;margin-top:-10px;margin-bottom:18px;font-size:1.1em;">Empowering Education & Technology</p>
        <div class="messages" id="messages">
            <div class="bot"><b>🤖 Paps Technologies Bot:</b> Hello! I am Paps Technologies Bot. Type 'bye' to exit.</div>
        </div>
        <form id="chat-form" autocomplete="off">
            <input type="text" id="user-input" placeholder="Type your message..." autofocus required />
            <button type="submit">Send</button>
        </form>
    </div>
    <script>
        const form = document.getElementById('chat-form');
        const input = document.getElementById('user-input');
        const messages = document.getElementById('messages');
        form.onsubmit = function(e) {
            e.preventDefault();
            const userMsg = input.value;
            messages.innerHTML += `<div class='user'><b>You:</b> ${userMsg}</div>`;
            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMsg })
            })
            .then(res => res.json())
            .then(data => {
                messages.innerHTML += `<div class='bot'><b>🤖 Paps Technologies Bot:</b> ${data.reply}</div>`;
                messages.scrollTop = messages.scrollHeight;
            });
            input.value = '';
        };
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    reply = get_bot_response(user_message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
