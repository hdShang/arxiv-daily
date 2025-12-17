---
layout: default
title: Context-Gated Cross-Modal Perception with Visual Mamba for PET-CT Lung Tumor Segmentation
---

# Context-Gated Cross-Modal Perception with Visual Mamba for PET-CT Lung Tumor Segmentation

**arXiv**: [2510.27508v1](https://arxiv.org/abs/2510.27508) | [PDF](https://arxiv.org/pdf/2510.27508.pdf)

**作者**: Elena Mulero Ayllón, Linlin Shen, Pierangelo Veltri, Fabrizia Gelardi, Arturo Chiti, Paolo Soda, Matteo Tortora

---

## 💡 一句话要点

**提出vMambaX框架以解决PET-CT肺肿瘤分割中模态融合挑战**

**关键词**: `肺肿瘤分割` `PET-CT融合` `跨模态感知` `Visual Mamba` `上下文门控`

## 📋 核心要点

1. 核心问题：PET和CT模态融合困难，影响肺肿瘤分割准确性。
2. 方法要点：基于Visual Mamba，引入上下文门控跨模态感知模块增强特征交互。
3. 实验或效果：在PCLT20K数据集上优于基线，计算复杂度低。

## 📄 摘要（原文）

> Accurate lung tumor segmentation is vital for improving diagnosis and
> treatment planning, and effectively combining anatomical and functional
> information from PET and CT remains a major challenge. In this study, we
> propose vMambaX, a lightweight multimodal framework integrating PET and CT scan
> images through a Context-Gated Cross-Modal Perception Module (CGM). Built on
> the Visual Mamba architecture, vMambaX adaptively enhances inter-modality
> feature interaction, emphasizing informative regions while suppressing noise.
> Evaluated on the PCLT20K dataset, the model outperforms baseline models while
> maintaining lower computational complexity. These results highlight the
> effectiveness of adaptive cross-modal gating for multimodal tumor segmentation
> and demonstrate the potential of vMambaX as an efficient and scalable framework
> for advanced lung cancer analysis. The code is available at
> https://github.com/arco-group/vMambaX.

