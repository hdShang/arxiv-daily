---
layout: default
title: Geodiffussr: Generative Terrain Texturing with Elevation Fidelity
---

# Geodiffussr: Generative Terrain Texturing with Elevation Fidelity

**arXiv**: [2511.23029v1](https://arxiv.org/abs/2511.23029) | [PDF](https://arxiv.org/pdf/2511.23029.pdf)

**作者**: Tai Inui, Alexander Matsumura, Edgar Simo-Serra

---

## 💡 一句话要点

**提出Geodiffussr流程，通过多尺度内容聚合生成符合数字高程图的纹理，用于可控2.5D地形生成。**

**关键词**: `地形生成` `纹理合成` `数字高程图` `流匹配` `多尺度聚合` `可控生成`

## 📋 核心要点

1. 核心问题：大规模地形生成依赖人工，需自动合成纹理并保持高程一致性。
2. 方法要点：使用流匹配和多尺度内容聚合，将DEM特征注入UNet块以强制高程一致性。
3. 实验或效果：相比基线，MCA显著提升视觉保真度和高度-外观耦合，FID降低49.16%。

## 📄 摘要（原文）

> Large-scale terrain generation remains a labor-intensive task in computer graphics. We introduce Geodiffussr, a flow-matching pipeline that synthesizes text-guided texture maps while strictly adhering to a supplied Digital Elevation Map (DEM). The core mechanism is multi-scale content aggregation (MCA): DEM features from a pretrained encoder are injected into UNet blocks at multiple resolutions to enforce global-to-local elevation consistency. Compared with a non-MCA baseline, MCA markedly improves visual fidelity and strengthens height-appearance coupling (FID $\downarrow$ 49.16%, LPIPS $\downarrow$ 32.33%, $Δ$dCor $\downarrow$ to 0.0016). To train and evaluate Geodiffussr, we assemble a globally distributed, biome- and climate-stratified corpus of triplets pairing SRTM-derived DEMs with Sentinel-2 imagery and vision-grounded natural-language captions that describe visible land cover. We position Geodiffussr as a strong baseline and step toward controllable 2.5D landscape generation for coarse-scale ideation and previz, complementary to physically based terrain and ecosystem simulators.

