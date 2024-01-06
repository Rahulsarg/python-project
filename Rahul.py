import tkinter
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import os
import datetime

# creat window
root = tkinter.Tk()
root.title("Exercise Recommender")   # title of gui
root.minsize(800, 700)
root.maxsize(1000, 1000)
root.config(background='lightsteelblue')

lbl_title = tkinter.Label(root, text="Exercise Recommender", font=("Verdana", 48), fg='black', bg='cornflowerblue')
lbl_title.pack(pady=(10, 20))

# lable to ask age
text_age = tkinter.Label(root, text="Enter your age", font=("Helvetica", 28), fg='black', bg='lightslategrey')
text_age.pack(pady=(2, 4))
text_age.place(x=50, y=150)
# age box
text_agebox = tkinter.Entry(root, width=25, bg='white', fg='black')
text_agebox.pack(pady=(14, 40))
text_agebox.place(x=290, y=157)

# lable to ask weight
text_weight = tkinter.Label(root, text="Enter your weight", font=("Helvetica", 28), fg='black', bg='lightslategrey')
text_weight.pack(pady=(70, 150))
text_weight.place(x=50, y=250)
# weight box
text_weightbox = tkinter.Entry(root, width=25, bg='white', fg='black')
text_weightbox.pack()
text_weightbox.place(x=290, y=257)

# label to ask height
text_height = tkinter.Label(root, text="Enter your height", font=("Helvetica", 28), fg='black', bg='lightslategrey')
text_height.pack(pady=(2, 4))
text_height.place(x=50, y=350)
# height box
text_heightbox = tkinter.Entry(root, width=25, bg='white', fg='black')
text_heightbox.pack()
text_heightbox.place(x=290, y=357)

# label to ask meal input 
text_meal = tkinter.Label(root, text="How much meal \nto be generated", font=("Helvetica", 28), fg='black', bg='lightslategrey')
text_meal.pack(pady=(2, 4))
text_meal.place(x=50, y=550)
# meal box
text_mealbox = tkinter.Entry(root, width=25, bg='white', fg='black')
text_mealbox.pack()
text_mealbox.place(x=290, y=557)

# radio button to get gender
text_gender = tkinter.Label(root, text="Enter your gender", font=("Helvetica", 28), fg='black', bg='lightslategrey')
text_gender.pack(pady=(2, 4))
text_gender.place(x=50, y=450)

gender_var = tkinter.StringVar()  # used of storing the value

male_radio = tkinter.Radiobutton(root, text="Male", variable=gender_var, value="male")
male_radio.pack()
male_radio.place(x=290, y=460)

female_radio = tkinter.Radiobutton(root, text="Female", variable=gender_var, value="female")
female_radio.pack()
female_radio.place(x=370, y=460)

gender_var.set("male") # setting the default value

# lable asking for cholestrol 
cholestrol_label = tkinter.Label(root, text='Select a specific cholesterol range')
cholestrol_label.pack()
cholestrol_label.place(x=550,y=127)
# option for dropdown menu
cholestrol_options = ['Below 200 mg/dL (5.2 mmol/L)', '200-239 mg/dL (5.2-6.2 mmol/L)', '240 mg/dL (6.2 mmol/L) and above']

cholestrol_var = tkinter.StringVar() # used for storing the value from input
# creating the dropdown
cholestrol_dropdown = ttk.Combobox(root, textvariable=cholestrol_var, values=cholestrol_options)
cholestrol_dropdown.pack()
cholestrol_dropdown.place(x=550,y=157)

# label asking for disease 
disease_label = tkinter.Label(root, text="Select a specific disease you have:", font=("Helvetica", 16))
disease_label.pack(pady=(20, 10))
disease_label.place(x=550,y=227)
# option for dropdown menu
disease_options = ['Cardiovascular Disease (heart)', 'Asthma', 'Arthritis', 'Diabetes', 'Osteoporosis', 'None of the above']

disease_var = tkinter.StringVar()
# creating the dropdown
disease_dropdown = ttk.Combobox(root, textvariable=disease_var, values=disease_options)
disease_dropdown.pack() 
disease_dropdown.place(x=550,y=257)

# label to get goals
goals_label = tkinter.Label(root, text="Select your personal health goal:", font=("Helvetica", 16))
goals_label.pack()
goals_label.place(x=550,y=327)
goals_options = ['Weight loss', 'Muscle gain', 'Cardiovascular fitness', 'Flexibility','Maintainence','General well-being', 'Custom']

goals_var = tkinter.StringVar()
# creating a dropdown menu
goals_dropdown = ttk.Combobox(root, textvariable=goals_var, values=goals_options)
goals_dropdown.pack()
goals_dropdown.place(x=550,y=357)
# box to get custum goal entry
custom_goal_entry = tkinter.Entry(root, width=20, bg='white', fg='black')
custom_goal_entry.pack()
custom_goal_entry.place(x=550,y=387)

# label to selete acivity level 
activity_label = tkinter.Label(root, text='Select a Acitvity level')
activity_label.pack()
activity_label.place(x=550,y=427)

activity_options = ['low','moderate','high']

activity_var = tkinter.StringVar()
activity_dropdown = ttk.Combobox(root, textvariable=activity_var, values=activity_options)
activity_dropdown.pack()
activity_dropdown.place(x=550,y=457)

# label to selecte acitvity level 
body_type_label = tkinter.Label(root, text='Select your body type')
body_type_label.pack()
body_type_label.place(x=550,y=527)

body_type_options = ['ectomorph','mesomorph','endomorph']

body_type_var = tkinter.StringVar()
body_type_dropdown = ttk.Combobox(root, textvariable=body_type_var, values=body_type_options)
body_type_dropdown.pack()
body_type_dropdown.place(x=550,y=557)

# creating the function to recommend exercise
def recommend_exercise():

    result_window = tkinter.Toplevel(root) #creating the new window over the root(main)window
    result_window.title("Exercise Recommender")
    result_window.geometry("600x350")
# getting the values from respective boxes 
    weight = float(text_weightbox.get())
    height = float(text_heightbox.get())
    cholesterol=str(cholestrol_var.get())
    disease=str(disease_var.get())

# formula of bmi
    bmi = (weight / (height * height))*10000
# printing the calulated bmi in result window
    result_label = tkinter.Label(result_window, text=f"Your BMI is {bmi:.2f}")
    result_label.pack(pady=20)

    # getting the values of selected from drop-down menu
    selected_cholesterol = cholestrol_var.get()
    selected_disease = disease_var.get()

        #display selected options

    cholestrol_label1= tkinter.Label(result_window, text=f"You selected Cholesterol Range: {selected_cholesterol}", font=("Helvetica", 16))
    cholestrol_label1.pack(pady=10)
# displaying the comment about the cholestrol input
    if selected_cholesterol== 'Below 200 mg/dL (5.2 mmol/L)' :
        ch_label=tkinter.Label(result_window,text="Your cholestrol is in desirable range ",font=("Helvetica", 16))
        ch_label.pack(pady=10)
    elif selected_cholesterol== '200-239 mg/dL (5.2-6.2 mmol/L)' :
        ch_label=tkinter.Label(result_window,text='Your cholestrol is in broderline range ',font=("Helvetica", 16))
        ch_label.pack(pady=10)
    else :
        ch_label=tkinter.Label(result_window,text='Your cholestrol level is high !!!',font=("Helvetica", 16))
        ch_label.pack(pady=10)
    disease_label1= tkinter.Label(result_window, text=f"You selected Disease: {selected_disease}", font=("Helvetica", 16))
    disease_label1.pack(pady=10)
# creating and appending the exercise the exercise according to bmi, cholestrol level, diesease
    exercise_recommendation =[]
    if bmi < 18.5:  # based on bmi 
        exercise_recommendation.append("brisk walking or jogging\n")
        if cholesterol == "Below 200 mg/dL (5.2 mmol/L)":
            exercise_recommendation.append( "Low-impact exercises: yoga or tai chi\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
        elif cholesterol == "200-239 mg/dL (5.2-6.2 mmol/L)":
            exercise_recommendation.append( "Interval training exercises: HIIT workouts\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
        else:
            exercise_recommendation.append( "High-intensity exercises: running or HIIT workouts\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")

    elif 18.5 <= bmi < 25:
        exercise_recommendation.append( "cycling or swimming\n")
        if cholesterol == "Below 200 mg/dL (5.2 mmol/L)":
            exercise_recommendation.append( "Low-impact exercises: yoga or tai chi\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
        elif cholesterol == "200-239 mg/dL (5.2-6.2 mmol/L)":
            exercise_recommendation.append( "Interval training exercises: HIIT workouts\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
        else:
            exercise_recommendation.append( "High-intensity exercises: running or HIIT workouts\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
    else:
        exercise_recommendation.append( "weightlifting\n")
        if cholesterol == "Below 200 mg/dL (5.2 mmol/L)":
            exercise_recommendation.append( "Low-impact exercises: yoga or tai chi\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
        elif cholesterol == "200-239 mg/dL (5.2-6.2 mmol/L)":
            exercise_recommendation.append( "Interval training exercises: HIIT workouts\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
        else:
            exercise_recommendation.append( "High-intensity exercises: running or HIIT workouts\n")
            if disease == "Cardiovascular Disease":
                exercise_recommendation.append( "Low-impact cardiovascular exercises: walking or swimming\n")
            elif disease == "Asthma":
                exercise_recommendation.append( "Low-intensity exercises: gentle yoga or stationary cycling\n")
            elif disease == "Arthritis":
                exercise_recommendation.append( "Joint-friendly exercises: water aerobics or tai chi\n")
    
    # join the the appends form about and displaying
    exercise_recommendation_str='\n'.join(exercise_recommendation)
    recommend=tkinter.Label(result_window,text=exercise_recommendation_str,font=("Verdana",16),bg='light blue')
    recommend.pack()
    
    # creating the function for getting the video
    def open_youtube_video():
        selected_goal = goals_var.get()
        goal_urls = {
                'Weight loss':'https://youtu.be/-YpRYNREDV8' ,
                'Muscle gain':'https://youtu.be/geK9GNKGRpo',
                'Cardiovascular fitness':'https://youtu.be/UfnKkdcvCMg' ,
                'Flexibility':'https://youtu.be/kCQ6irSQwYA' ,
                'General well-being':'https://youtu.be/z_jjX-i45hU' 
            }
            # creating the custom goal entry 
        if selected_goal == 'Custom':
            custom_goal = custom_goal_entry.get()
            if custom_goal:
                webbrowser.open([custom_goal])
            else:
                error_label = tkinter.Label(result_window, text="Please enter a custom goal.", font=("Helvetica", 14), fg='red', bg='white')
                error_label.pack()
        elif selected_goal in goal_urls:
            webbrowser.open(goal_urls[selected_goal])
        else:
            error_label = tkinter.Label(result_window, text="No YouTube video available for the selected goal.", font=("Helvetica", 14), fg='red', bg='white')
            error_label.pack()

    open_video_button = tkinter.Button(result_window, text="Open YouTube Video", command=open_youtube_video)
    open_video_button.pack()

    # creating the function to generate the meal plan
    def generate_meal_plan():
        goal = goals_var.get()
        activity = activity_var.get()
        weight = float(text_weightbox.get())

        # Calculate daily maximum calories
        if activity== 'low':
            activity_factor = 1.2
        elif activity == 'moderate':
            activity_factor = 1.55
        elif activity_var== 'high':
            activity_factor = 1.9
        else:
            print("Invalid activity level entered. Assuming moderate activity.")
            activity_factor = 1.55

        if goal == 'weight_gain':
            daily_calories = weight * 18 * activity_factor
        elif goal == 'weight_loss':
            daily_calories = weight * 14 * activity_factor
        elif goal == 'maintenance':
            daily_calories = weight * 16 * activity_factor
        else:
            print("Invalid fitness goal entered. Assuming weight maintenance.")
            daily_calories = weight * 16 * activity_factor

    # Calculate macronutrient ranges
        daily_min_fat = 0.2 * daily_calories / 9
        daily_max_protein = weight * 1.2
        daily_min_carbs = (daily_calories - (daily_min_fat * 9) - (daily_max_protein * 4)) / 4
        daily_max_carbs = (daily_calories - (daily_min_fat * 9) - (daily_max_protein * 4)) / 4

    # Generate the meal plan for the specified number of meals
        num_meals = int(text_mealbox.get())
        meal_plan = []
        for i in range(num_meals):
            meal = f"Meal {i+1}: Protein - {daily_max_protein/num_meals:.2f}g, Carbs - {daily_max_carbs/num_meals:.2f}g, Fat - {daily_min_fat/num_meals:.2f}g"
            meal_plan.append(meal)

        # creating the window to display the text of meal plan
        window = tkinter.Toplevel(root)
        window.title('Meal Planner')  

        # creating the text box for displaying the generated meal plan
        result_text = tkinter.Text(window, height=10, width=50)
        result_text.pack()

        # inserting the values of meal plan in text box
        result_text.delete('1.0', tkinter.END)
        result_text.insert(tkinter.END, "Daily Maximum Calories: " + str(daily_calories) + "\n")
        result_text.insert(tkinter.END, "Daily Minimum Fat: " + str(daily_min_fat) + "\n")
        result_text.insert(tkinter.END, "Daily Maximum Protein: " + str(daily_max_protein) + "\n")
        result_text.insert(tkinter.END, "Daily Minimum Carbs: " + str(daily_min_carbs) + "\n")
        result_text.insert(tkinter.END, "Daily Maximum Carbs: " + str(daily_max_carbs) + "\n")
        result_text.insert(tkinter.END, "Meal Plan for " + str(num_meals) + " meals:\n")
        for meal in meal_plan:
            result_text.insert(tkinter.END, meal + "\n")

        # function for saving the values
        def save_file(name_entry):
            # getting name 
            name = name_entry.get()
            # creating the directory
            directory = 'exercise_recommendations'
            os.makedirs(directory, exist_ok=True)
            # getting current date time
            now = datetime.datetime.now()

            # creating the path wiht file name according to users name
            filename = f"{name}_file.txt"
            filepath = os.path.join(directory, filename)

            # Open the file in write mode with UTF-8 encoding
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Your BMI is {bmi:.2f}\n")
                file.write(f"You selected Cholesterol Range: {selected_cholesterol}\n\n")
                file.write("Exercise Recommendations:\n")
                file.write(exercise_recommendation_str)

             # File has been created and written with the user's name as the file name

            # displaying the message that data had been saves
            messagebox.showinfo("File Saved", "The file has been saved successfully.")

        # Creating the function to name the file
        def name_file():
            # creating prompt window to get name of user
            prompt = tkinter.Toplevel(result_window)
            name_label = tkinter.Label(prompt, text="Enter your name:")
            name_label.pack()
            name_entry = tkinter.Entry(prompt)
            name_entry.pack()
            # real save button to save the button
            save_button = tkinter.Button(prompt, text="Save", command=lambda: save_file(name_entry))
            save_button.pack()
        # Save button to open prompt to get name
        save_button = tkinter.Button(result_window, text="Save", command=name_file)
        save_button.pack()

        window.mainloop()# to run the window in loop 
    # button the generate the meal plan 
    generate_button = tkinter.Button(result_window, text="Generate Meal Plan", command=generate_meal_plan)
    generate_button.pack()
    # to run the resutl window in loop 
    result_window.mainloop()
# button to recommend exercise 
bmi_btn = tkinter.Button(root, text='Recommend Exercise', command=recommend_exercise)
bmi_btn.pack()
bmi_btn.place(x=330, y=650)
# to run the root window in loop 
root.mainloop()
