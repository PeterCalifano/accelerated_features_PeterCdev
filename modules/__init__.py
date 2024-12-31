"""
	"XFeat: Accelerated Features for Lightweight Image Matching, CVPR 2024."
	https://www.verlab.dcc.ufmg.br/descriptors/xfeat_cvpr24/
"""
from .xfeat import XFeat
from .lighterglue import LighterGlue
from .model import XFeatModel

__all__ = ['XFeat', 'LighterGlue', 'XFeatModel']
