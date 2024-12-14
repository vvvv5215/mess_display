from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

odd_week_menu = {
    'Monday': {
        'Breakfast': ['Pongal', 'Vada(2)', 'Sambar', 'G Chutney', 'Bbj', 'Sprouts', 'Banana(1)', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Bhindi Fry', 'Rice', 'Sambar', 'Rasam', 'Curd', 'Gongura Pickle', 'Papad'],
        'Snacks': ['Pasta', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Chapati', 'Aloo Mattar', 'Tamarind Rice', 'Buttermilk', 'Fryums']
    },
    'Tuesday': {
        'Breakfast': ['Idli', 'Rice Bonda', 'Sambar', 'C Chutney', 'Bbj', 'Sprouts', 'Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Beans Carrot Poriyal', 'Rice', 'Andhra Tomato Dal', 'Rasam', 'Curd', 'Fryums'],
        'Snacks': ['Aloo Bonda', 'Sauce', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Chole Bature', 'Onion Mint Salad', 'White Rice', 'Snake Gourd Kootu', 'Butter Milk', 'Rasam']
    },
    'Wednesday': {
        'Breakfast': ['Poori', 'Aloo Channa Masala', 'Bbj', 'Sprouts', 'Banana(1)', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Onion Pakoda', 'Rice', 'Vathakolambu', 'Rasam', 'Masala Papad', 'Tomato Pickle'],
        'Snacks': ['Boiled Groundnuts', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Pulka', 'Veg Biryani', 'Raita', 'Papad', 'Buttermilk']
    },
    'Thursday': {
        'Breakfast': ['Wheat Rava Upma', 'Poha', 'Mysore Bonda', 'C Chutney', 'Bbj', 'Sprouts', 'Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Kadai Paneer', 'Rice', 'Masala Sambar', 'Curd', 'Fryums', 'Mango Pickle'],
        'Snacks': ['Sweet Corn (Plate Price 6cm)', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Tawa Chapathi', 'Kal Dosa', 'Tomato Chutney', 'Onion Salad']
    },
    'Friday': {
        'Breakfast': ['Idly', 'Vada(2)', 'Sambar', 'G Chutney', 'Bbj', 'Sprouts', 'Banana(1)', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Jeera Rice', 'Beetroot Poriyal', 'Rice', 'Rasam', 'Curd', 'Papad', 'Mango Pickle'],
        'Snacks': ['Onion Pakoda', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Phulka', 'Veg Pulao', 'Raita']
    },
    'Saturday': {
        'Breakfast': ['Aloo Paratha', 'Channa Masala', 'Raita', 'Pickle', 'Bbj', 'Sprouts', 'Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Lauki Chana Dal', 'Gobi 65', 'Rice', 'Sambar', 'Rasam', 'Curd', 'Fryums'],
        'Snacks': ['Millet Snack', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Pulka', 'Chitnind Paneer', 'Bagara Rice', 'Buttermilk']
    },
    'Sunday': {
        'Breakfast': ['Rava Dosa', 'Upma', 'Sambar', 'C Chutney', 'Bbj', 'Sprouts', 'Seasonal Cut Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Paneer Butter Masala', 'Kaju Curry', 'Veg Biryani', 'Onion Raitha', 'Tawa Chapati'],
        'Snacks': ['Pani Puri', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Chapatti', 'Aloo Mattar', 'Tamarind Rice', 'Buttermilk', 'Fryums', 'Seasonal Cut Fruits']
    }
}

even_week_menu = {
    'Monday': {
        'Breakfast': ['Pesarattu', 'Upma', 'Sambar', 'G Chutney', 'Bbj', 'Peanuts/Poridge', 'Banana(1)', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Aloo Masala Wedges', 'Rice', 'Vathakolambu', 'Curd', 'Fryums', 'Gongura Pickle'],
        'Snacks': ['Standard Salad', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Tawa Chapathi', 'Mixed Veg Kurma', 'Lemon Rice', 'Curd Rice', 'Mango Pickle', 'Kheer']
    },
    'Tuesday': {
        'Breakfast': ['Poori', 'Aloo Curry', 'Bbj', 'Sprouts', 'Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Keerai(Spinach) Poriyal', 'Rice', 'Rasam', 'Curd', 'Papad', 'Tomato Pickle'],
        'Snacks': ['Mirchi Bajji(2)', 'C Chutney', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Phulka', 'Aloo Bhindi Dry', 'Tomato Rice', 'Pickle', 'Raita', 'Gulab Jamun(2)']
    },
    'Wednesday': {
        'Breakfast': ['Masala Dosa', 'Sambar', 'C Chutney', 'Bbj', 'Sprouts', 'Banana(1)', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Kovakkai Fry', 'Rice', 'Curd', 'Rasam', 'Fryums', 'Tomato Pickle'],
        'Snacks': ['Seasoned Fruit Juice', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Pulka', 'Veg Pulao', 'Raita', 'Sambar Rice', 'Curd Rice', 'Special Dinner']
    },
    'Thursday': {
        'Breakfast': ['Chow Chow Bath', 'Mysore Bonda(2)', 'C Chutney', 'Bbj', 'Sprouts', 'Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Bhindi Masala Curry', 'Rice', 'Mixed Veg Kurakkozhammi', 'Rasam', 'Curd', 'Papad', 'Gongura Chutney'],
        'Snacks': ['Mix Veg Maggi(130g)', 'Tomato Sauce', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Plain Rice', 'Mixed Dal', 'Pickle', 'Sambar Rice', 'Curd Rice', 'Boost']
    },
    'Friday': {
        'Breakfast': ['Rava Idly', 'Vada(2)', 'Sambar', 'G Chutney', 'Bbj', 'Sprouts', 'Banana(1)', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Rice', 'Gobi Fry', 'Andhra Tomato Dal', 'Rasam', 'Curd', 'Fryums'],
        'Snacks': ['Muskmelon Juice', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Sweet Corn', 'Special Dinner', 'Rasam']
    },
    'Saturday': {
        'Breakfast': ['Tawa Chapathi', 'Aloo Dry', 'Curd', 'Pickle', 'Bbj', 'Sprouts', 'Cut Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Chilli Soya Bean Dry', 'Perugu Pachadi', 'Rice', 'Sambar', 'Rasam', 'Curd', 'Papad', 'Mango Pickle'],
        'Snacks': ['Banana Juice', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Plain Rice', 'Mixed Dal', 'Butter Milk', 'Kheer']
    },
    'Sunday': {
        'Breakfast': ['Set Dosa', 'Sambar', 'G Chutney', 'Bbj', 'Sprouts', 'Seasonal Cut Fruits', 'Tea, Coffee, Milk, Sugar, Salt'],
        'Lunch': ['Tawa Chapathi', 'Paneer/Gobi Curry', 'Veg Biryani', 'Raitha'],
        'Snacks': ['Pani Puri', 'Tea, Coffee, Milk, Sugar'],
        'Dinner': ['Idly', 'Sambar', 'Peerkangai Kootu', 'Curd Rice', 'Mango Pickle', 'Kheer']
    }
}


@app.route('/')
def showmess():
    today = datetime.now().strftime('%A')
    week_number = datetime.now().isocalendar()[1]
    is_odd_week = week_number % 2 != 0

    menu = odd_week_menu if is_odd_week else even_week_menu
    todays_menu = menu.get(today, {})

    return render_template('showmess.html', 
                           day=today,
                           week_type="Odd Week" if is_odd_week else "Even Week",
                           breakfast="<br>".join(todays_menu.get('Breakfast', ["No breakfast available"])),
                           lunch="<br>".join(todays_menu.get('Lunch', ["No lunch available"])),
                           snacks="<br>".join(todays_menu.get('Snacks', ["No snacks available"])),
                           dinner="<br>".join(todays_menu.get('Dinner', ["No dinner available"]))
                          )

if __name__ == '__main__':
    app.run(debug=True)
