import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import anvil.server

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )
  # Send yourself an email each time feedback is submitted
  anvil.email.send(to="ab.rdx.tnt@gmail.com", # Change this to your email address!
                   subject=f"Feedback from {name}",
                   text=f""" A new person has filled out the feedback form! Name: {name} Email address: {email} Feedback: {feedback} """)