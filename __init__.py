# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TweetImage
                                 A QGIS plugin
 Tweets an image of your current map canvas
                             -------------------
        begin                : 2015-12-08
        copyright            : (C) 2015 by ajggeoger
        email                : llansteffan@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TweetImage class from file TweetImage.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tweet_image import TweetImage
    return TweetImage(iface)
