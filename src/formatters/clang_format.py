# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    clang_format.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 10:40:07 by cacharle          #+#    #+#              #
#    Updated: 2020/10/05 08:27:48 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import subprocess


def clang_format(content: str) -> str:
    """ Wrapper around the clang-format command

        Pass content on stdin and return stdout

        Note:
            Need to put .clang-format in user's home directory
            since clang-format doesn't allow to specify
            the path to a configuration file
    """

    process = subprocess.Popen(
        ["clang-format", "-style=file"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    out, _ = process.communicate(input=content.encode())
    return out.decode()
