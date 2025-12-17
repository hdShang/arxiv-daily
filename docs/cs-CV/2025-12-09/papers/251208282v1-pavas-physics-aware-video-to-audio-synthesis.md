---
layout: default
title: PAVAS: Physics-Aware Video-to-Audio Synthesis
---

# PAVAS: Physics-Aware Video-to-Audio Synthesis

**arXiv**: [2512.08282v1](https://arxiv.org/abs/2512.08282) | [PDF](https://arxiv.org/pdf/2512.08282.pdf)

**作者**: Oh Hyun-Bin, Yuhta Takida, Toshimitsu Uesaka, Tae-Hyun Oh, Yuki Mitsufuji

---

## 💡 一句话要点

**提出PAVAS方法，通过物理感知适配器将物理推理融入视频到音频合成，以提升声音的物理真实性。**

**关键词**: `视频到音频合成` `物理感知生成` `扩散模型` `物体交互` `音频物理一致性`

## 📋 核心要点

1. 现有视频到音频生成模型多基于外观驱动，忽略物理因素对声音的影响。
2. PAVAS引入物理驱动音频适配器，利用视觉语言模型和3D重建估计物体质量与速度，指导音频合成。
3. 实验基于VGG-Impact基准和APCC指标，显示PAVAS在物理合理性和感知一致性上优于现有模型。

## 📄 摘要（原文）

> Recent advances in Video-to-Audio (V2A) generation have achieved impressive perceptual quality and temporal synchronization, yet most models remain appearance-driven, capturing visual-acoustic correlations without considering the physical factors that shape real-world sounds. We present Physics-Aware Video-to-Audio Synthesis (PAVAS), a method that incorporates physical reasoning into a latent diffusion-based V2A generation through the Physics-Driven Audio Adapter (Phy-Adapter). The adapter receives object-level physical parameters estimated by the Physical Parameter Estimator (PPE), which uses a Vision-Language Model (VLM) to infer the moving-object mass and a segmentation-based dynamic 3D reconstruction module to recover its motion trajectory for velocity computation. These physical cues enable the model to synthesize sounds that reflect underlying physical factors. To assess physical realism, we curate VGG-Impact, a benchmark focusing on object-object interactions, and introduce Audio-Physics Correlation Coefficient (APCC), an evaluation metric that measures consistency between physical and auditory attributes. Comprehensive experiments show that PAVAS produces physically plausible and perceptually coherent audio, outperforming existing V2A models in both quantitative and qualitative evaluations. Visit https://physics-aware-video-to-audio-synthesis.github.io for demo videos.

