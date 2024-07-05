from nada_dsl import *


def initialize_parties(nr_participants):
   return [Party(name=f"Participant{i}") for i in range(nr_participants)]


def input_feedback(nr_participants, nr_projects, participants):
   feedback = []
   for p in range(nr_projects):
       project_feedback = []
       for i in range(nr_participants):
           rating = SecretUnsignedInteger(Input(name=f"rating{p}_{i}", party=participants[i]))
           influence = SecretUnsignedInteger(Input(name=f"influence{p}_{i}", party=participants[i]))  # Adjusted to ensure uniqueness
           project_feedback.append(rating * influence)
       feedback.append(project_feedback)
   return feedback

def feedback_results(participants, feedback, nr_projects):
   results = []
   for p in range(nr_projects):
       total_score = UnsignedInteger(0)
       for f in feedback[p]:
           total_score += f
       results.append(Output(total_score, name=f"final_score_p{p}", party=Party(name="ResultsParty")))
   return results

def nada_main():
   nr_participants = 10
   nr_projects = 5
   participants = initialize_parties(nr_participants)
   project_feedback = input_feedback(nr_participants, nr_projects, participants)
  
   final_results = feedback_results(participants, project_feedback, nr_projects)
   return final_results 