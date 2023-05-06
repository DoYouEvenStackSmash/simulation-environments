#!/usr/bin/python3
from render_support import PygameArtFxns as pafn
from render_support import GeometryFxns as gfn
from render_support import MathFxns as mfn
from render_support import TransformFxns as tfn
from support.transform_polygon import *
from support.Polygon import *

class RigidBody:
  LINE_LEN = 30
  def __init__(self, 
              parent_agent,
              rigid_link = None,
              ref_origin = (0,0),
              endpoint = (0,0),
              ref_center = (0,0),
              point_set = [],
              rel_theta = 0
              ):
    self.parent_agent = parent_agent
    self.origin = ref_origin
    self.endpoint = endpoint
    self.ref_center = ref_center
    self.point_set = point_set
    self.body = rigid_link
    self.rel_theta = rel_theta
  

  def get_rel_theta(self):
    '''
    Accessor for relative angle
    returns an angle theta in radians
    '''
    return self.rel_theta

  def get_body(self):
    '''
    Accessor for internal polygon
    Returns a polygon object or None
    '''
    return self.body

  def get_points(self):
    '''
    Wrapper for points access
    '''
    if self.body == None:
      return self.get_point_set()
    return self.get_body_points()
  
  def get_point_set(self):
    '''
    Accessor for the point set which is constrained to the RigidBody
    Returns a list of points
    '''
    return self.point_set
  
  def get_body_points(self):
    '''
    Get internal point set
    returns a list of points
    '''
    return self.body.dump_points()
  
  def get_relative_angle(self):
    '''
    Accessor for the RigidBody's angle relative to previous RigidBody
    Returns an angle theta
    '''
    return self.rel_theta
  
  def get_center(self):
    '''
    Accessor for the RigidBody's origin
    returns a point
    '''
    return self.ref_center

  def get_endpoint(self):
    '''
    Accessor for the RigidBody endpoint
    Returns a point
    '''
    return self.endpoint
  
  def get_origin(self):
    '''
    Accessor for an origin point
    returns a point
    '''
    return self.origin


  def rotate_body(self, target_point):
    '''
    Rotation for the rigid body
    '''
    rotation = self.get_relative_rotation(target_point)
    rot_mat = tfn.calculate_rotation_matrix(rotation, 1)    
    self.endpoint = tfn.rotate_point(self.get_center(), self.get_endpoint(), rot_mat)
    self.origin = tfn.rotate_point(self.get_center(), self.get_origin(), rot_mat)
    rotate_polygon(self.body, rot_mat, self.get_center())
    self.rel_theta += rotation
    return rotation


  def translate_body(self, target_point):
    '''
    Translates internal polygon
    Does not return
    '''
    theta, r = mfn.car2pol(self.get_center(), target_point)
    pt2 = mfn.pol2car(self.get_center(), r, theta)
    cx,cy = self.get_center()

    x_disp,y_disp = pt2[0] - cx, pt2[1] - cy
    self.endpoint = mfn.pol2car(self.endpoint, r, theta)
    self.origin = mfn.pol2car(self.origin, r, theta)
    self.ref_center = mfn.pol2car(self.ref_center, r, theta)
    
    translate_polygon(self.body, x_disp, y_disp)
    return (theta, r)
    

  def update_orientation(self, point_set, theta):
    '''
    TODO rotate by angle
    '''
    self.point_set = point_set
    self.rel_theta = theta
  
  def update_point_set(self, point_set):
    '''
    Replace existing point set with a new point set.
    Used during rotations
    Does not return
    '''
    self.point_set = point_set

  def get_normals(self):
    '''
    Calculates coordinate axes x,y in R2
    Returns a pair of points representing axis unit endpoints
    '''
    ox,oy = self.get_center()
    theta = self.rel_theta
    xx,xy = RigidBody.LINE_LEN * np.cos(theta), RigidBody.LINE_LEN * np.sin(theta)
    yx,yy = RigidBody.LINE_LEN * np.cos(theta + np.pi / 2), RigidBody.LINE_LEN * np.sin(theta + np.pi / 2)
    return ((xx+ox,xy+oy), (yx+ox,yy+oy))

  def get_relative_rotation(self, target_point):
    '''
    Given a target point, computes the angle theta between the current
    endpoint and the target point for use during rotation

    Returns a normalized angle theta
    '''
  
    norm, dist = mfn.car2pol(self.get_center(), self.get_endpoint())
    rad, r = mfn.car2pol(self.get_center(), target_point)
    
    norm = mfn.correct_angle(norm)
    rad = mfn.correct_angle(rad)
    
    rotation = np.subtract(rad,norm)
    
    # correction for arctan identification
    if rotation > np.pi:
      rotation = rotation - 2 * np.pi
    if rotation < -np.pi:
      rotation = rotation + 2 * np.pi
    
    return rotation

    