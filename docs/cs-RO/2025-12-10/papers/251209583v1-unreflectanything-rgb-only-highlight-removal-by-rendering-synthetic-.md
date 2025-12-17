---
layout: default
title: UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision
---

# UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision

**arXiv**: [2512.09583v1](https://arxiv.org/abs/2512.09583) | [PDF](https://arxiv.org/pdf/2512.09583.pdf)

**作者**: Alberto Rota, Mert Kiray, Mert Asim Karaoglu, Patrick Ruhkamp, Elena De Momi, Nassir Navabm, Benjamin Busam

---

## 💡 一句话要点

**提出UnReflectAnything框架，通过渲染合成高光监督从单张RGB图像中去除高光**

**关键词**: `高光去除` `RGB图像处理` `合成数据渲染` `视觉Transformer` `令牌级修复` `手术图像分析`

## 📋 核心要点

1. 核心问题：高光在自然和手术图像中扭曲外观、遮挡纹理并阻碍几何推理
2. 方法要点：使用冻结视觉Transformer编码器提取特征，结合轻量级头部定位高光区域和令牌级修复模块恢复特征
3. 实验或效果：在多个基准测试中达到竞争性性能，并泛化到自然和手术领域

## 📄 摘要（原文）

> Specular highlights distort appearance, obscure texture, and hinder geometric reasoning in both natural and surgical imagery. We present UnReflectAnything, an RGB-only framework that removes highlights from a single image by predicting a highlight map together with a reflection-free diffuse reconstruction. The model uses a frozen vision transformer encoder to extract multi-scale features, a lightweight head to localize specular regions, and a token-level inpainting module that restores corrupted feature patches before producing the final diffuse image. To overcome the lack of paired supervision, we introduce a Virtual Highlight Synthesis pipeline that renders physically plausible specularities using monocular geometry, Fresnel-aware shading, and randomized lighting which enables training on arbitrary RGB images with correct geometric structure. UnReflectAnything generalizes across natural and surgical domains where non-Lambertian surfaces and non-uniform lighting create severe highlights and it achieves competitive performance with state-of-the-art results on several benchmarks. Project Page: https://alberto-rota.github.io/UnReflectAnything/

