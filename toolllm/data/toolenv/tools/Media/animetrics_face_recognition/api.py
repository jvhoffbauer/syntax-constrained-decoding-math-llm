import requests
import json
from datetime import date, datetime, timedelta
import os

from typing import Optional, Dict, Union, List


def add_to_gallery(subject_id: str, gallery_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Adds an already enrolled Subject into an existing or uncreated Gallery.  Galleries that don't exist will automatically be created."
    subject_id: The ID used to previously enroll some person (subject)
        gallery_id: A unique ID indicating the collection to which the subject should be added.  If this gallery doesn't exist, it will be created.
        
    """
    url = f"https://animetrics.p.rapidapi.com/add_to_gallery"
    querystring = {'subject_id': subject_id, 'gallery_id': gallery_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def assign_face_to_subject(subject_id: str, face_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Assign Face ID to a Subject ID. This operation will change the Subject ID associated with an individual Face ID. The Face ID that is required should be taken from the response of a previous enrollment. Assigning a Face ID to a new Subject ID who belongs to more than one gallery will affect that Subject's identity in each gallery. This operation might be used if several pictures of an individual are enrolled and then later it is found out that one of these pictures was in fact someone else."
    subject_id: unique subject ID to replace that of a previous enrollment
        face_id: face ID from the response of a previous enrollment
        
    """
    url = f"https://animetrics.p.rapidapi.com/assign_face_to_subject"
    querystring = {'subject_id': subject_id, 'face_id': face_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_enroll(image_id: str, subject_id: str, gallery_id: str, topleftx: int=None, toplefty: int=None, width: int=None, height: int=None, lefteyecenterx: int=None, lefteyecentery: int=None, righteyecenterx: int=None, righteyecentery: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Computes a biometric signature for a known face ("subject") in a picture and adds it to a collection ("gallery") for later searching. The subject id and gallery id must be supplied in addition to an image id reference from a previous Detect or Detect Features call. A subject id must be a globally unique identifier for each known individual identity for each API key. Subjects may exist in more than one gallery and can be added to or removed from a gallery with the Add To Gallery and Remove From Gallery functions. Adding multiple pictures of the same subject will help improve matching accuracy. Similarly, adding pictures of different people with the same subject id will negatively affect the accuracy of the matching algorithm. Enroll operations also require a face hint describing which face in a picture is to be enrolled. This may be in the form of face bounds (topLeftX, topLeftY, width, height) or eye coordinates (leftEyeCenterX, leftEyeCenterY, rightEyeCenterX, rightEyeCenterY). These landmarks may all be taken from the output of Detect or Detect Features calls."
    image_id: an image ID that was returned from a detect operation
        subject_id: a unique ID describing this person
        gallery_id: a unique ID indicating the collection to which the person should be enrolled
        topleftx: X-Coordinate for top left corner of face. May be modified from Detect output
        toplefty: Y-Coordinate for top left corner of face. May be modified from Detect output
        width: Width of face. May be modified from Detect output
        height: Height of face. May be modified from Detect output
        lefteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the left eye center. May be modified from Detect output
        lefteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the left eye center. May be modified from Detect output
        righteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the right eye center. May be modified from Detect output
        righteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the right eye center. May be modified from Detect output
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/enroll"
    querystring = {'image_id': image_id, 'subject_id': subject_id, 'gallery_id': gallery_id, }
    if topleftx:
        querystring['topLeftX'] = topleftx
    if toplefty:
        querystring['topLeftY'] = toplefty
    if width:
        querystring['width'] = width
    if height:
        querystring['height'] = height
    if lefteyecenterx:
        querystring['leftEyeCenterX'] = lefteyecenterx
    if lefteyecentery:
        querystring['leftEyeCenterY'] = lefteyecentery
    if righteyecenterx:
        querystring['righteyeCenterX'] = righteyecenterx
    if righteyecentery:
        querystring['rightEyeCenterY'] = righteyecentery
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_recognize(gallery_id: str, image_id: str=None, face_id: str=None, max_num_results: int=None, topleftx: int=None, toplefty: str=None, height: int=None, lefteyecenterx: int=None, lefteyecentery: int=None, righteyecenterx: int=None, righteyecentery: int=None, width: int=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Matches an unknown face against a collection ("gallery") of known faces. Galleries are built using the Enroll function. Response includes a similarity score between 0 and 1 for all closely matching subjects in the gallery. A gallery id must be supplied in addition to an image id reference from a previous Detect or Detect Features call. Recognize operations require a face hint describing which face in a picture is to be enrolled. This may be in the form of face bounds (topLeftX, topLeftY, width, height) or eye coordinates (leftEyeCenterX, leftEyeCenterY, rightEyeCenterX, rightEyeCenterY). These landmarks may all be taken from the output of Detect or Detect Features calls."
    gallery_id: a unique ID indicating the collection which this unknown person should be compared against
        image_id: (required if face_id is omitted) image ID that was returned from a detect operation
        face_id: (required if image_id omitted) face ID from the response of a previous enrollment
        max_num_results: the maximum number of matches returned by this search (default 10)
        topleftx: X-Coordinate for top left corner of face. May be modified from Detect output
        toplefty: Y-Coordinate for top left corner of face. May be modified from Detect output
        height: Height of face. May be modified from Detect output
        lefteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the left eye center. May be modified from Detect output
        lefteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the left eye center. May be modified from Detect output
        righteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the right eye center. May be modified from Detect output
        righteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the right eye center. May be modified from Detect output
        width: Width of face. May be modified from Detect output
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/recognize"
    querystring = {'gallery_id': gallery_id, }
    if image_id:
        querystring['image_id'] = image_id
    if face_id:
        querystring['face_id'] = face_id
    if max_num_results:
        querystring['max_num_results'] = max_num_results
    if topleftx:
        querystring['topLeftX'] = topleftx
    if toplefty:
        querystring['topLeftY'] = toplefty
    if height:
        querystring['height'] = height
    if lefteyecenterx:
        querystring['leftEyeCenterX'] = lefteyecenterx
    if lefteyecentery:
        querystring['leftEyeCenterY'] = lefteyecentery
    if righteyecenterx:
        querystring['rightEyeCenterX'] = righteyecenterx
    if righteyecentery:
        querystring['rightEyeCenterY'] = righteyecentery
    if width:
        querystring['width'] = width
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_remove_from_gallery(subject_id: str, gallery_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Removes an already enrolled Subject from an existing Gallery. If this is the only subject in that Gallery, the Gallery will be deleted. If the Subject exists in no other Galleries, he will be deleted from the Face Recognition System."
    subject_id: The ID used to previously enroll some person ("subject")
        gallery_id: A unique ID indicating the collection from which the subject should be removed. If the subject exists in no other galleries, the biometric template will be removed from the Facial Recognition System and subsequent Add To Gallery operations for this subject will fail.
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/remove_from_gallery"
    querystring = {'subject_id': subject_id, 'gallery_id': gallery_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_usage(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve your current daily and monthly count of function calls made to the api. Total, billable, detect, enroll and recognize counts are displayed."
    
    """
    url = f"https://animetrics.p.rapidapi.com/v2/usage"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_view_gallery(gallery_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "View the subject ids that have been enrolled in a specific gallery."
    gallery_id: A unique ID indicating the gallery to query.
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/view_gallery"
    querystring = {'gallery_id': gallery_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_view_subject(subject_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "View the face ids that have been enrolled in a specific subject."
    subject_id: unique subject ID that matches one or more previous enrollments
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/view_subject"
    querystring = {'subject_id': subject_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_add_to_gallery(subject_id: str, gallery_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Adds an already enrolled Subject into an existing or uncreated Gallery. Galleries that don't exist will automatically be created."
    subject_id: The ID used to previously enroll some person ("subject")
        gallery_id: A unique ID indicating the collection to which the subject should be added. If this gallery doesn't exist, it will be created.
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/add_to_gallery"
    querystring = {'subject_id': subject_id, 'gallery_id': gallery_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_assign_face_to_subject(face_id: str, subject_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Assign Face ID to a Subject ID. This operation will change the Subject ID associated with an individual Face ID. The Face ID that is required should be taken from the response of a previous enrollment. Assigning a Face ID to a new Subject ID who belongs to more than one gallery will affect that Subject's identity in each gallery. This operation might be used if several pictures of an individual are enrolled and then later it is found out that one of these pictures was in fact someone else."
    face_id: face ID from the response of a previous enrollment
        subject_id: unique subject ID to replace that of a previous enrollment
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/assign_face_to_subject"
    querystring = {'face_id': face_id, 'subject_id': subject_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def recognize(gallery_id: str='Family_Members', image_id: str='7245253dbd2a142ceb40e031cb173734', topleftx: int=105, toplefty: int=188, width: int=123, height: int=123, lefteyecenterx: int=139, lefteyecentery: int=160, righteyecenterx: int=198, righteyecentery: int=164, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Matches an unknown face against a collection ("gallery") of known faces. Galleries are built using the Enroll function. Response includes a similarity score between 0 and 1 for all closely matching subjects in the gallery.  A gallery id must be supplied in addition to an image id reference from a previous Detect or Detect Features call. Recognize operations require a face hint describing which face in a picture is to be enrolled. This may be in the form of face bounds (topLeftX, topLeftY, width, height) or eye coordinates (leftEyeCenterX, leftEyeCenterY, rightEyeCenterX, rightEyeCenterY). These landmarks may all be taken from the output of Detect or Detect Features calls."
    gallery_id: a unique ID indicating the collection which this unknown person should be compared against
        image_id: an image ID that was returned from a detect operation
        topleftx: X-Coordinate for top left corner of face. May be modified from Detect output.
        toplefty: Y-Coordinate for top left corner of face. May be modified from Detect output.
        width: Width of face. May be modified from Detect output.
        height: Height of face. May be modified from Detect output.
        lefteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the left eye center. May be modified from Detect output.
        lefteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the left eye center. May be modified from Detect output.
        righteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the right eye center. May be modified from Detect output.
        righteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the right eye center. May be modified from Detect output.
        
    """
    url = f"https://animetrics.p.rapidapi.com/recognize"
    querystring = {}
    if gallery_id:
        querystring['gallery_id'] = gallery_id
    if image_id:
        querystring['image_id'] = image_id
    if topleftx:
        querystring['topLeftX'] = topleftx
    if toplefty:
        querystring['topLeftY'] = toplefty
    if width:
        querystring['width'] = width
    if height:
        querystring['height'] = height
    if lefteyecenterx:
        querystring['leftEyeCenterX'] = lefteyecenterx
    if lefteyecentery:
        querystring['leftEyeCenterY'] = lefteyecentery
    if righteyecenterx:
        querystring['rightEyeCenterX'] = righteyecenterx
    if righteyecentery:
        querystring['rightEyeCenterY'] = righteyecentery
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def remove_from_gallery(subject_id: str, gallery_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Removes an already enrolled Subject from an existing Gallery.  If this is the only subject in that Gallery, the Gallery will be deleted.  If the Subject exists in no other Galleries, he will be deleted from the Face Recognition System."
    subject_id: The ID used to previously enroll some person (subject)
        gallery_id: A unique ID indicating the collection from which the subject should be removed.  If the subject exists in no other galleries, his biometric template will be removed from the Facial Recognition System and subsequent Add To Gallery operations for this subject will fail.
        
    """
    url = f"https://animetrics.p.rapidapi.com/remove_from_gallery"
    querystring = {'subject_id': subject_id, 'gallery_id': gallery_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def usage(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Retrieve your current daily and monthly count of function calls made to the api. Total, billable, detect, enroll and recognize counts are displayed."
    
    """
    url = f"https://animetrics.p.rapidapi.com/usage"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def verify(subject_id_of_target: str, subject_id_of_unknown: str='John_Doe', toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Verify if an unknown face (or collection of faces of an unknown individual) has the same identity as a claimed target. A similarity score is returned, and is optimized for discriminating the target subject from other individuals. Note that there must be at least two faces of the target subject enrolled."
    subject_id_of_target: A unique subject ID of the known person (must have at least 2 faces enrolled)
        subject_id_of_unknown: A unique subject ID of the person who's identity is to be verified
        
    """
    url = f"https://animetrics.p.rapidapi.com/verify"
    querystring = {'subject_id_of_target': subject_id_of_target, }
    if subject_id_of_unknown:
        querystring['subject_id_of_unknown'] = subject_id_of_unknown
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def view_gallery(gallery_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "View the subject ids that have been enrolled in a specific gallery."
    gallery_id: a unique ID indicating the gallery to query
        
    """
    url = f"https://animetrics.p.rapidapi.com/view_gallery"
    querystring = {'gallery_id': gallery_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def view_subject(subject_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "View the face ids that have been enrolled in a specific subject."
    subject_id: unique subject ID that matches one or more previous enrollments
        
    """
    url = f"https://animetrics.p.rapidapi.com/view_subject"
    querystring = {'subject_id': subject_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def enroll(subject_id: str='John_Doe', gallery_id: str='Family_Members', image_id: str='7245253dbd2a142ceb40e031cb173734', topleftx: int=105, toplefty: int=188, width: int=123, height: int=123, lefteyecenterx: int=139, lefteyecentery: int=160, righteyecenterx: int=198, righteyecentery: int=164, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Computes a biometric signature for a known face ("subject") in a picture and adds it to a collection ("gallery") for later searching. The subject id and gallery id must be supplied in addition to an image id reference from a previous Detect or Detect Features call. A subject id must be a globally unique identifier for each known individual identity for each API key. Subjects may exist in more than one gallery and can be added to or removed from a gallery with the Add To Gallery and Remove From Gallery functions. Adding multiple pictures of the same subject will help improve matching accuracy. Similarly, adding pictures of different people with the same subject id will negatively affect the accuracy of the matching algorithm.  Enroll operations also require a face hint describing which face in a picture is to be enrolled. This may be in the form of face bounds (topLeftX, topLeftY, width, height) or eye coordinates (leftEyeCenterX, leftEyeCenterY, rightEyeCenterX, rightEyeCenterY). These landmarks may all be taken from the output of Detect or Detect Features calls."
    subject_id: a unique ID describing this person
        gallery_id: a unique ID indicating the collection to which the person should be enrolled
        image_id: an image ID that was returned from a detect operation
        topleftx: X-Coordinate for top left corner of face. May be modified from Detect output.
        toplefty: Y-Coordinate for top left corner of face. May be modified from Detect output.
        width: Width of face. May be modified from Detect output.
        height: Height of face. May be modified from Detect output.
        lefteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the left eye center. May be modified from Detect output.
        lefteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the left eye center. May be modified from Detect output.
        righteyecenterx: (required if face coordinates/dimensions omitted) X-Coordinate for the right eye center. May be modified from Detect output.
        righteyecentery: (required if face coordinates/dimensions omitted) Y-Coordinate for the right eye center. May be modified from Detect output.
        
    """
    url = f"https://animetrics.p.rapidapi.com/enroll"
    querystring = {}
    if subject_id:
        querystring['subject_id'] = subject_id
    if gallery_id:
        querystring['gallery_id'] = gallery_id
    if image_id:
        querystring['image_id'] = image_id
    if topleftx:
        querystring['topLeftX'] = topleftx
    if toplefty:
        querystring['topLeftY'] = toplefty
    if width:
        querystring['width'] = width
    if height:
        querystring['height'] = height
    if lefteyecenterx:
        querystring['leftEyeCenterX'] = lefteyecenterx
    if lefteyecentery:
        querystring['leftEyeCenterY'] = lefteyecentery
    if righteyecenterx:
        querystring['rightEyeCenterX'] = righteyecenterx
    if righteyecentery:
        querystring['rightEyeCenterY'] = righteyecentery
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def list_galleries(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Lists the galleries that have been created by your personal API key."
    
    """
    url = f"https://animetrics.p.rapidapi.com/list_galleries"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_list_galleries(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Lists the galleries that have been created by your personal API key."
    
    """
    url = f"https://animetrics.p.rapidapi.com/v2/list_galleries"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def delete_face(face_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Delete a Face from a known Subject. This operation will only delete the individual Face that is associated with an enrollment transaction for a Subject. The Face ID that is required should be taken from the response of a previous enrollment. Deleteing a Face from a Subject who belongs to more than one gallery will affect that Subject's identity in each gallery. This operation might be used if several pictures of an individual are enrolled and then later it is found out that one of these pictures was in fact someone else who's identity is unknown."
    face_id: face ID from the response of a previous enrollment
        
    """
    url = f"https://animetrics.p.rapidapi.com/delete_face"
    querystring = {'face_id': face_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def v2_delete_face(face_id: str, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Delete a Face from a known Subject. This operation will only delete the individual Face that is associated with an enrollment transaction for a Subject. The Face ID that is required should be taken from the response of a previous enrollment. Deleteing a Face from a Subject who belongs to more than one gallery will affect that Subject's identity in each gallery. This operation might be used if several pictures of an individual are enrolled and then later it is found out that one of these pictures was in fact someone else who's identity is unknown."
    face_id: Delete a Face from a known Subject. This operation will only delete the individual Face that is associated with an enrollment transaction for a Subject. The Face ID that is required should be taken from the response of a previous enrollment. Deleteing a Face from a Subject who belongs to more than one gallery will affect that Subject's identity in each gallery. This operation might be used if several pictures of an individual are enrolled and then later it is found out that one of these pictures was in fact someone else who's identity is unknown.
        
    """
    url = f"https://animetrics.p.rapidapi.com/v2/delete_face"
    querystring = {'face_id': face_id, }
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "animetrics.p.rapidapi.com"
        }


    response = requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

