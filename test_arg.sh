usage() { echo "Usage: $0 [-t <image tag name:version>]" 1>&2; exit 1; }

while getopts t: flag
do
    case "${flag}" in
        t) t=${OPTARG};;
    esac
done

if [ -z "${t}" ]
  then
    usage
fi

echo "${t}"
