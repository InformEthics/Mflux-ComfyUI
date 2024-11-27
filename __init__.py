from .Mflux_Comfy.Mflux_Air import QuickMfluxNode, MfluxModelsLoader, MfluxModelsDownloader, MfluxCustomModels
from .Mflux_Comfy.Mflux_Pro import MfluxImg2Img, MfluxLorasLoader, MfluxControlNetLoader

NODE_CLASS_MAPPINGS = {
    "QuickMfluxNode": QuickMfluxNode,
    "MfluxModelsLoader": MfluxModelsLoader,
    "MfluxModelsDownloader": MfluxModelsDownloader,
    "MfluxCustomModels": MfluxCustomModels,
    "MfluxImg2Img": MfluxImg2Img,
    "MfluxLorasLoader": MfluxLorasLoader,
    "MfluxControlNetLoader": MfluxControlNetLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QuickMfluxNode": "Quick MFlux Generation",
    "MfluxModelsLoader": "MFlux Models Loader",
    "MfluxModelsDownloader": "MFlux Models Downloader",
    "MfluxCustomModels": "MFlux Custom Models",
    "MfluxImg2Img": "MFlux Image-to-Image",
    "MfluxLorasLoader": "MFlux Loras Loader",
    "MfluxControlNetLoader": "MFlux ControlNet Loader",
}
