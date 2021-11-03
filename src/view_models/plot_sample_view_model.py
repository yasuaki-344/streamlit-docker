"""View model のサンプル."""
import dataclasses


@dataclasses.dataclass
class PlotSampleViewModel:
    """Plot sample ページのためのview model."""

    gradient: float
    intercept: float
