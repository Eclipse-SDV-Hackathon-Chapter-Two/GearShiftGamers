# Podman build

podman build -t keyboard_adapter -f keyboard.dockerfile .

# store podman
podman save -o keyboard_adapter.tar keyboard_adapter:latest

# git LFS for podman images
sudo apt install git-lfs
git lfs install
git lfs track "*.tar"
git add .gitattributes keyboard_adapter.tar
git commit -m "Add container image with Git LFS"
git push