MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
(cd "${MY_DIR}"/_build/html || exit;
python3 -m http.server 8000
)
