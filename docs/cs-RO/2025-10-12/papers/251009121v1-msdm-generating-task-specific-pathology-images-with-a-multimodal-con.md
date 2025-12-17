---
layout: default
title: MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation
---

# MSDM: Generating Task-Specific Pathology Images with a Multimodal Conditioned Diffusion Model for Cell and Nuclei Segmentation

**arXiv**: [2510.09121v1](https://arxiv.org/abs/2510.09121) | [PDF](https://arxiv.org/pdf/2510.09121.pdf)

**作者**: Dominik Winter, Mai Bui, Monica Azqueta Gavaldon, Nicolas Triltsch, Marco Rosati, Nicolas Brieu

---

## 💡 一句话要点

**提出多模态语义扩散模型以生成病理图像-掩码对，提升细胞和核分割性能**

**关键词**: `计算病理学` `扩散模型` `图像生成` `细胞分割` `多模态学习` `数据增强`

## 📋 核心要点

1. 细胞和核分割面临标注数据稀缺问题，尤其对罕见形态
2. 模型融合形态、颜色和元数据，通过多模态条件扩散生成图像-掩码对
3. 合成数据显著改善分割模型准确性，如柱状细胞，并验证与真实数据相似性

## 📄 摘要（原文）

> Scarcity of annotated data, particularly for rare or atypical morphologies,
> present significant challenges for cell and nuclei segmentation in
> computational pathology. While manual annotation is labor-intensive and costly,
> synthetic data offers a cost-effective alternative. We introduce a Multimodal
> Semantic Diffusion Model (MSDM) for generating realistic pixel-precise
> image-mask pairs for cell and nuclei segmentation. By conditioning the
> generative process with cellular/nuclear morphologies (using horizontal and
> vertical maps), RGB color characteristics, and BERT-encoded assay/indication
> metadata, MSDM generates datasests with desired morphological properties. These
> heterogeneous modalities are integrated via multi-head cross-attention,
> enabling fine-grained control over the generated images. Quantitative analysis
> demonstrates that synthetic images closely match real data, with low
> Wasserstein distances between embeddings of generated and real images under
> matching biological conditions. The incorporation of these synthetic samples,
> exemplified by columnar cells, significantly improves segmentation model
> accuracy on columnar cells. This strategy systematically enriches data sets,
> directly targeting model deficiencies. We highlight the effectiveness of
> multimodal diffusion-based augmentation for advancing the robustness and
> generalizability of cell and nuclei segmentation models. Thereby, we pave the
> way for broader application of generative models in computational pathology.

