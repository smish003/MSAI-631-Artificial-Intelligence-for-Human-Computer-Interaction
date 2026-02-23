
### Adaptive Design Approach
For this task, I used the recommendations system I developed for the previous week's assignment. The original system was designed to recommend movies using a content-based approach that uses machine learning techniques. The system includes a graphical user interface that allows users to select a movie and receive a list of recommended movie titles. While the application is interactive and responds to user input, the recommendation logic is static, that is, the same input consistently produces the same output as shown in Figure 1, and the system does not learn from user behavior. <br/> <br/> 
To transform the system into an AI-based adaptive human-computer interaction system, adaptive behavior was incorporated into the existing application during runtime. The system was extended to observe user interactions, such as movie selections and interactions with recommended titles, and use this information as implicit feedback. Based on these interactions, the system dynamically adjusts recommendation rankings by updating a runtime user preference profile. This profile stores interaction frequency and influences future recommendation ordering. As a result, the same movie selection can produce different outputs over time, demonstrating real-time adaptation rather than static similarities as shown in Figure 2.<br/> <br/> 

By reusing and extending an existing system rather than designing from scratch, this project demonstrates how an adaptive user interface can be effectively integrated into previously developed applications, enhancing user experience through intelligent and responsive interaction. 

<img width="975" height="728" alt="image" src="https://github.com/user-attachments/assets/c577bff8-c712-4de2-a2d2-b21e1e54b54c" />

Figure 1: Initially Developed Recommended System

Once the code changes are done, the user first selects Inception and requests recommendations. After clicking a recommended title such as ‘The Avengers’, ‘Iron Man’, etc., as shown in Figure 2, the user clicks on Iron Man to open the corresponding IMDb link, and then the system records this user interaction as implicit feedback. When the user clicks the Recommend button again, the system re-ranks the recommendation based on the recorded interaction, resulting in modified output as shown in Figure 3. 
<img width="975" height="728" alt="image" src="https://github.com/user-attachments/assets/e7000956-77ec-4793-a46b-9c9f9e1aa288" />
Figure 2: Adaptive System

<img width="979" height="725" alt="image" src="https://github.com/user-attachments/assets/c75bd893-13a6-4e47-a9c8-0b9860615650" />
Figure 3: Updated Recommendation
