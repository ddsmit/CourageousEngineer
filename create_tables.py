print(__name__)

from chrissmit import db, bcrypt
from chrissmit.services.db_models import User, Reasons, Tags

db.drop_all()
db.create_all()

yolanda = User(
    authorization_level=bcrypt.generate_password_hash('all_access'),
    full_name='Yolanda Smit',
    twitter_handle='@yoyosmit',
    email='yolanda.smit@courageousengineer.com',
    image_file = 'yoyo.svg',
    password = bcrypt.generate_password_hash('M!$$y0y0'),
    linkedin = 'https://www.linkedin.com/in/yolanda-smit-cqe-ssgb-ab911314/',
    content = """
    Yolanda Smit is a Quality Leader in the industrial manufacturing segment with 12+ years of experience in agricultural, automotive, and medical equipment manufacturing.  Yolanda has extensive experience in quality management, project management, operational excellence, continuous improvement, manufacturing quality, and supplier quality.  
</p>
Yolanda is energized about solving real world problems in the manufacturing and transactional spaces.  She specializes in training and coaching others on the best manufacturing quality practices, creating and implementing standard work, utilizing Lean and Six Sigma methodologies to lead multifaceted interdisciplinary projects in the manufacturing and transactional spaces and establishing KPI’s to drive and monitor process and organizational performance. 
</p>
Yolanda is the proud product of an HBCU education, she graduated Magna Cum Laude from Johnson C. Smith University in Charlotte, NC with a Bachelor of Science in Computer Engineering and a Bachelor of Science in Mathematics.  Yolanda also possesses a Master of Science in Quality Assurance from California State University and is an ASQ Certified Quality Engineer and Six Sigma Green Belt. 
</p>
Yolanda was born and raised on St. Thomas, United States Virgin Islands.  Her Caribbean upbringing instilled the values that continue to keep her focused and driven.  She embodies her mantras “Speak with Courage” and “Lead Authentically”.  As engineers we have a responsibility to be courageous in our thoughts and actions.  Courage is a catalyst of creativity and innovation; courage can be the spark which invokes introspective thoughts and candid discussions.  Whether you are a people leader or individual contributor you must remain true to who you are.  Being your authentic self while exhibiting servant leadership.
    """
)

david = User(
    authorization_level=bcrypt.generate_password_hash('all_access'),
    full_name='David Smit',
    twitter_handle='@davidouglasmit',
    email='david.smit@courageousengineer.com',
    image_file = 'yoyo.svg',
    password = bcrypt.generate_password_hash('P@$$w0rd%12'),
    linkedin = 'https://www.linkedin.com/in/david-smit-b8220ba6/',
    content = """
    David Smit is an engineer not only by trade, but by heart. David has always had a love for tinkering from programming a Tomogatchi clone in BASIC to building, racing, and modifying hobby class RC cars, and building and programming Lego Mindstorm Robots. 
</p>
David grew his knowledge and love for engineering at Iowa State University, where he earned a Bachelors in  Mechanical Engineering. Since then, he has worked in Manufacturing and Product Development on various products including Chillers for HVAC systems, IVT Transmissions for John Deere tractors, and front and rear drive axles for SUV's.
</p>
David re-ignited his love for programming when he started his most recent role as a Product Development Engineer. He found that the tools that were being used for data analysis were cumbersome and inefficient. He decided to try Python per a suggestion from a friend he had met at an equipment supplier, and he's loved using the language ever since.
</p>
David has expanded his use of Python from Data analysis at work to web development. He built this site in Flask as a Christmas present to his wonderful wife, Yolanda Smit. He has continued to learn and expand his knowledge of web development (HTML, CSS, JS) and has also started learning Machine Learning tooling. 

    """,
)

db.session.add(yolanda)
db.session.add(david)

choices=[
    'Feedback',
    'Inquire About Mentorship',
    'Help',
    'I Want to Join the Team',
    ]

for choice in choices:
    new_record = Reasons(
        desc=choice,
    )
    db.session.add(new_record)

choices=[
    'Race',
    'Gender',
    'Orientation',
    'Background',
    'Culture',
    'Self',
    ]

for choice in choices:
    new_record = Tags(
        desc=choice,
    )
    db.session.add(new_record)

db.session.commit()
