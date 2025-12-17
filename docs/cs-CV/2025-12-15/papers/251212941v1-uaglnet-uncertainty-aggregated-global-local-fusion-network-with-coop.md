---
layout: default
title: UAGLNet: Uncertainty-Aggregated Global-Local Fusion Network with Cooperative CNN-Transformer for Building Extraction
---

# UAGLNet: Uncertainty-Aggregated Global-Local Fusion Network with Cooperative CNN-Transformer for Building Extraction

**arXiv**: [2512.12941v1](https://arxiv.org/abs/2512.12941) | [PDF](https://arxiv.org/pdf/2512.12941.pdf)

**作者**: Siyuan Yao, Dongxiu Liu, Taotao Li, Shengjie Li, Wenqi Ren, Xiaochun Cao

---

## 💡 一句话要点

**提出UAGLNet，通过不确定性聚合的全局-局部融合网络解决遥感图像建筑提取中的结构复杂性问题。**

**关键词**: `建筑提取` `遥感图像` `全局-局部融合` `不确定性建模` `CNN-Transformer合作` `语义分割`

## 📋 核心要点

1. 核心问题：现有方法因特征金字塔间隙和全局-局部特征融合不足，导致建筑提取结果不准确和模糊。
2. 方法要点：设计合作编码器结合CNN和Transformer，引入全局-局部融合模块和不确定性聚合解码器以提升语义质量和减少不确定性。
3. 实验或效果：在广泛实验中，UAGLNet优于其他先进方法，代码已开源。

## 📄 摘要（原文）

> Building extraction from remote sensing images is a challenging task due to the complex structure variations of the buildings. Existing methods employ convolutional or self-attention blocks to capture the multi-scale features in the segmentation models, while the inherent gap of the feature pyramids and insufficient global-local feature integration leads to inaccurate, ambiguous extraction results. To address this issue, in this paper, we present an Uncertainty-Aggregated Global-Local Fusion Network (UAGLNet), which is capable to exploit high-quality global-local visual semantics under the guidance of uncertainty modeling. Specifically, we propose a novel cooperative encoder, which adopts hybrid CNN and transformer layers at different stages to capture the local and global visual semantics, respectively. An intermediate cooperative interaction block (CIB) is designed to narrow the gap between the local and global features when the network becomes deeper. Afterwards, we propose a Global-Local Fusion (GLF) module to complementarily fuse the global and local representations. Moreover, to mitigate the segmentation ambiguity in uncertain regions, we propose an Uncertainty-Aggregated Decoder (UAD) to explicitly estimate the pixel-wise uncertainty to enhance the segmentation accuracy. Extensive experiments demonstrate that our method achieves superior performance to other state-of-the-art methods. Our code is available at https://github.com/Dstate/UAGLNet

