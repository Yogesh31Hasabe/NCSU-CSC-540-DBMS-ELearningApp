from datetime import datetime
class UserDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_faculty(self, first_name, last_name, email, password):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO Faculty (faculty_id, first_name, last_name, email, password, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            first_part = first_name[:2].lower()
            last_part = last_name[:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")
            faculty_id = f"{first_part}{last_part}{month}{year}"

            values = (faculty_id, first_name, last_name, email, password, created_at, updated_at)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def create_student(self, first_name, last_name, email, password, role):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO Student (user_id, first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            first_part = first_name[:2].lower()
            last_part = last_name[:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")
            user_id = f"{first_part}{last_part}{month}{year}"

            values = (user_id, first_name, last_name, email, password, role)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def create_ta(self, first_name, last_name, email, password, role):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO TA (user_id, first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            first_part = first_name[:2].lower()
            last_part = last_name[:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")
            user_id = f"{first_part}{last_part}{month}{year}"

            values = (user_id, first_name, last_name, email, password, role)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def get_user_by_id(self, user_id):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = "SELECT * FROM User WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    def update_user(self, user_id, first_name, last_name, email, role):
        try:
            cursor = self.db_connection.cursor()
            query = """
            UPDATE User
            SET first_name = %s, last_name = %s, email = %s, role = %s
            WHERE user_id = %s
            """
            values = (first_name, last_name, email, role, user_id)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def delete_user(self, user_id):
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM User WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def validate_credentials(self, user_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM User WHERE user_id = %s AND password = %s"
            cursor.execute(query, (user_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Exception as e:
            print(f"Error validating admin credentials: {e}")
            return False
        
    def validate_credentials_ta(self, ta_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM TA WHERE ta_id = %s AND password = %s"
            cursor.execute(query, (ta_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Exception as e:
            print(f"Error validating TA credentials: {e}")
            return False

    def enroll(self, first_name, last_name, email, course_token):
        try:
            cursor = self.db_connection.cursor()
            query = '''
            SELECT u.user_id
            FROM User u
            JOIN Student_Enrolls_ActiveCourse seac ON u.user_id = seac.user_id
            WHERE u.email = %s;
            '''
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False

    def add_new_etextbook(self, title, etextbook_id):
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO Textbook  (textbook_id, title) VALUES (%s, %s)"
            cursor.execute(query, (etextbook_id, title))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
    
            
        
    def add_new_chapter(self, textbook_id, chapter_id, chapter_title):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO Chapter (textbook_id, chapter_id, title, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, chapter_title, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
        
    def add_new_content_block(self, textbook_id, chapter_id, section_id, section_title):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO Section (textbook_id, chapter_id, section_id, title, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, section_title, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
    
    def add_new_text(self, textbook_id, chapter_id, section_id, block_id, text):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            type_of_block = "text"
            hidden = "no"
            query = "INSERT INTO Blocks (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, type_of_block, text, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Text added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
    
    def add_new_picture(self, textbook_id, chapter_id, section_id, block_id, content):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            type_of_block = "picture"
            hidden = "no"
            query = "INSERT INTO Blocks (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Text added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e

    def add_question(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id, qa):
        try:
            cursor = self.db_connection.cursor()
            question_id = qa[0]
            question_text = qa[1]
            option1_text = qa[2]
            option1_explanation = qa[3]
            option2_text = qa[4]
            option2_explanation = qa[5]
            option3_text = qa[6]
            option3_explanation = qa[7]
            option4_text = qa[8]
            option4_explanation = qa[9]
            answer = qa[10]
            
            query = "INSERT INTO Question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, question_text, option_1, explanation_1, option_2, explanation_2, option_3, explanation_3, option_4, explanation_4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, question_text, option1_text, option1_explanation, option2_text, option2_explanation, option3_text, option3_explanation, option4_text, option4_explanation, answer))
            self.db_connection.commit()
            cursor.close()            
            return True, "Question added successfully"  
        except Exception as e:  
            print(f"Error adding new question: {e}")
            return False, e
        
    
    def add_activity(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            hidden = "no"
            query = "INSERT INTO Activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, unique_activity_id, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Activity added successfully"
        except Exception as e:
            print(f"Error adding new activity: {e}")
            return False, e 
        
    def add_activityBlock(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            hidden = "no"
            content = unique_activity_id
            type_of_block = "activity"
            query = "INSERT INTO Blocks (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Activity block added successfully"
        except Exception as e:
            print(f"Error adding new activity block: {e}")
            return False, e 
    
    def checkTextbook(self, etextbook_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Textbook WHERE textbook_id = %s"
            cursor.execute(query, (etextbook_id,))
            textbook = cursor.fetchone()
            cursor.close()
            if textbook:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking textbook: {e}")
            return False
    
    def checkChapter(self, textbook_id, chapter_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Chapter WHERE textbook_id = %s AND chapter_id = %s"
            cursor.execute(query, (textbook_id, chapter_id,))
            chapter = cursor.fetchone()
            cursor.close()
            if chapter:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking chapter: {e}")
            return False
    
    def checkSection(self, textbook_id, chapter_id, section_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s"
            cursor.execute(query, (textbook_id, chapter_id, section_id,))
            section = cursor.fetchone()
            cursor.close()
            if section:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking section: {e}")
            return False        
    
    def checkBlock(self, textbook_id, chapter_id, section_id, block_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Blocks WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id,))
            block = cursor.fetchone()
            cursor.close()
            if block:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking block: {e}")
            return False  
    
    def checkFaculty(self, faculty_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Faculty WHERE faculty_id = %s"
            cursor.execute(query, (faculty_id,))
            textbook = cursor.fetchone()
            cursor.close()
            if textbook:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking faculty: {e}")
            return False  
    
    def add_active_course(self, course_id, course_name, etextbook_id, course_start_date, course_end_date, unique_token, course_capacity, faculty_id):
        try:
            cursor = self.db_connection.cursor()    
            current_date = datetime.now()           
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            course_type = "Active"
            query = "INSERT INTO Course (course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (course_id, course_name, etextbook_id, course_type, faculty_id, None, course_start_date, course_end_date, unique_token, course_capacity, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Active Course added successfully"
        except Exception as e:
            print(f"Error adding active course: {e}")
            return False, e
    
    def add_evaluation_course(self, course_id, course_name, etextbook_id, course_start_date, course_end_date, faculty_id):
        try:
            cursor = self.db_connection.cursor()    
            current_date = datetime.now()           
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            course_type = "Evaluation"
            query = "INSERT INTO Course (course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (course_id, course_name, etextbook_id, course_type, faculty_id, None, course_start_date, course_end_date, None, None, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Evaluation Course added successfully"
        except Exception as e:
            print(f"Error adding evaluation course: {e}")
            return False, e