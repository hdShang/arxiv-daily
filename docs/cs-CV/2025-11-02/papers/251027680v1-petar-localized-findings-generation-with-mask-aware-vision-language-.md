---
layout: default
title: PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting
---

# PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting

**arXiv**: [2510.27680v1](https://arxiv.org/abs/2510.27680) | [PDF](https://arxiv.org/pdf/2510.27680.pdf)

**作者**: Danyal Maqbool, Changhee Lee, Zachary Huemann, Samuel D. Church, Matthew E. Larson, Scott B. Perlman, Tomas A. Romero, Joshua D. Warner, Meghan Lubner, Xin Tie, Jameson Merkow, Junjie Hu, Steve Y. Cho, Tyler J. Bradshaw

---

## 💡 一句话要点

**提出PETAR-4B模型，结合PET/CT与病灶轮廓，生成局部化PET自动报告。**

**关键词**: `3D医学影像` `视觉语言模型` `PET/CT报告生成` `病灶分割` `多模态推理` `自动化评估`

## 📋 核心要点

1. 核心问题：3D PET/CT数据大、病灶小且分散，报告冗长，现有视觉语言模型多限于2D。
2. 方法要点：构建大规模数据集，集成PET、CT和病灶轮廓，实现空间接地报告生成。
3. 实验或效果：自动和人工评估显示，PETAR显著提升报告质量，推进3D医学视觉语言理解。

## 📄 摘要（原文）

> Recent advances in vision-language models (VLMs) have enabled impressive
> multimodal reasoning, yet most medical applications remain limited to 2D
> imaging. In this work, we extend VLMs to 3D positron emission tomography and
> computed tomography (PET/CT), a domain characterized by large volumetric data,
> small and dispersed lesions, and lengthy radiology reports. We introduce a
> large-scale dataset comprising over 11,000 lesion-level descriptions paired
> with 3D segmentations from more than 5,000 PET/CT exams, extracted via a hybrid
> rule-based and large language model (LLM) pipeline. Building upon this dataset,
> we propose PETAR-4B, a 3D mask-aware vision-language model that integrates PET,
> CT, and lesion contours for spatially grounded report generation. PETAR bridges
> global contextual reasoning with fine-grained lesion awareness, producing
> clinically coherent and localized findings. Comprehensive automated and human
> evaluations demonstrate that PETAR substantially improves PET/CT report
> generation quality, advancing 3D medical vision-language understanding.

