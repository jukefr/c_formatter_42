{
  lib,
  python3Packages,
  fetchFromGitHub,
  pkgs,
}:

python3Packages.buildPythonApplication rec {
  pname = "c-formatter-42";
  version = "0.2.7";
  pyproject = true;

  src = fetchFromGitHub {
    owner = "jukefr";
    repo = "c_formatter_42";
    rev = "db2dfedfd851c0b1d525060de289d3ae6ea33452";
    sha256 = "0x92kj32apvcd86yyplzwzrly5ya0snf1q00nvi1c27vdq45aipa";
  };

  build-system = with python3Packages; [
    setuptools
    wheel
  ];

  dependencies = with pkgs; [ clang-tools ];

  meta = with lib; {
    description = "C language formatter for 42 norminette";
    homepage = "https://github.com/jukefr/c_formatter_42";
    license = licenses.gpl3;
    maintainers = with maintainers; [ jukefr ];
  };

}
