# Container commands

## Podman build

``
podman build -t keyboard_adapter -f keyboard.dockerfile .
``

## store podman

``
podman save -o keyboard_adapter.tar keyboard_adapter:latest
``

## git LFS for podman images

````
sudo apt install git-lfs
git lfs install
git lfs track "*.tar"
git add .gitattributes keyboard_adapter.tar
git commit -m "Add container image with Git LFS"
git push
````

## databroker

``
docker run -it --rm --name Server --network kuksa -p 55555:55555 ghcr.io/eclipse-kuksa/kuksa-databroker:main --insecure
``



# start keyboard_adapter
xhost + && podman run --rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix keyboard_adapter

# start blobby
podman run --rm -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e XDG_RUNTIME_DIR=/run/user/$(id -u) \
    -v /run/user/$(id -u):/run/user/$(id -u) \
    --device /dev/snd \
    -e PULSE_SERVER=unix:/run/user/$(id -u)/pulse/native \
    -v /run/user/$(id -u)/pulse/native:/run/user/$(id -u)/pulse/native \
    -v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
    blobbyvolley2 blobby
