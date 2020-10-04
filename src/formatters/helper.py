# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    helper.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 11:38:00 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 13:47:23 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import re


def local_scope(func):
    def wrapper(content: str) -> str:
        return re.sub(
            r"\n\{\n(?P<body>.*?)\n\}\n".replace(r"\n", "\n"),
            lambda match: "\n{\n" + func(match.group("body")) + "\n}\n",
            content,
            flags=re.DOTALL
        )
    return wrapper