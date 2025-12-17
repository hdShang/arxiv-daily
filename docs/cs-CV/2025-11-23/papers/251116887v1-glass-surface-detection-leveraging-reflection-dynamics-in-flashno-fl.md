---
layout: default
title: Glass Surface Detection: Leveraging Reflection Dynamics in Flash/No-flash Imagery
---

# Glass Surface Detection: Leveraging Reflection Dynamics in Flash/No-flash Imagery

**arXiv**: [2511.16887v1](https://arxiv.org/abs/2511.16887) | [PDF](https://arxiv.org/pdf/2511.16887.pdf)

**作者**: Tao Yan, Hao Huang, Yiwei Lu, Zeyu Wang, Ke Xu, Yinghui Wang, Xiaojun Chang, Rynson W. H. Lau

---

## 💡 一句话要点

**提出NFGlassNet方法，利用闪光/无闪光图像中的反射动态检测玻璃表面。**

**关键词**: `玻璃表面检测` `闪光/无闪光图像` `反射动态` `NFGlassNet` `计算机视觉`

## 📋 核心要点

1. 玻璃表面检测因无色透明特性而具挑战性，现有方法依赖边界或反射线索但未充分利用玻璃内在属性。
2. 基于闪光/无闪光图像中反射动态，设计反射对比挖掘模块和反射引导注意力模块以提升检测精度。
3. 构建3.3K图像对数据集，实验表明方法优于现有先进技术，代码和数据集将公开。

## 📄 摘要（原文）

> Glass surfaces are ubiquitous in daily life, typically appearing colorless, transparent, and lacking distinctive features. These characteristics make glass surface detection a challenging computer vision task. Existing glass surface detection methods always rely on boundary cues (e.g., window and door frames) or reflection cues to locate glass surfaces, but they fail to fully exploit the intrinsic properties of the glass itself for accurate localization. We observed that in most real-world scenes, the illumination intensity in front of the glass surface differs from that behind it, which results in variations in the reflections visible on the glass surface. Specifically, when standing on the brighter side of the glass and applying a flash towards the darker side, existing reflections on the glass surface tend to disappear. Conversely, while standing on the darker side and applying a flash towards the brighter side, distinct reflections will appear on the glass surface. Based on this phenomenon, we propose NFGlassNet, a novel method for glass surface detection that leverages the reflection dynamics present in flash/no-flash imagery. Specifically, we propose a Reflection Contrast Mining Module (RCMM) for extracting reflections, and a Reflection Guided Attention Module (RGAM) for fusing features from reflection and glass surface for accurate glass surface detection. For learning our network, we also construct a dataset consisting of 3.3K no-flash and flash image pairs captured from various scenes with corresponding ground truth annotations. Extensive experiments demonstrate that our method outperforms the state-of-the-art methods. Our code, model, and dataset will be available upon acceptance of the manuscript.

