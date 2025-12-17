---
layout: default
title: VLM2GeoVec: Toward Universal Multimodal Embeddings for Remote Sensing
---

# VLM2GeoVec: Toward Universal Multimodal Embeddings for Remote Sensing

**arXiv**: [2512.11490v1](https://arxiv.org/abs/2512.11490) | [PDF](https://arxiv.org/pdf/2512.11490.pdf)

**作者**: Emanuel Sánchez Aimar, Gulnaz Zhambulova, Fahad Shahbaz Khan, Yonghao Xu, Michael Felsberg

---

## 💡 一句话要点

**提出VLM2GeoVec，通过单编码器统一嵌入多模态遥感数据，实现可扩展检索与区域级空间推理。**

**关键词**: `遥感视觉语言模型` `多模态嵌入` `对比学习` `区域级推理` `地理空间检索`

## 📋 核心要点

1. 遥感图像与自然图像差异显著，现有方法在检索与生成任务间存在割裂。
2. VLM2GeoVec采用单编码器处理交错输入，通过对比损失训练统一向量空间。
3. 在RSMEB基准上，区域级检索任务性能显著提升，同时保持传统任务竞争力。

## 📄 摘要（原文）

> Satellite imagery differs fundamentally from natural images: its aerial viewpoint, very high resolution, diverse scale variations, and abundance of small objects demand both region-level spatial reasoning and holistic scene understanding. Current remote-sensing approaches remain fragmented between dual-encoder retrieval models, which excel at large-scale cross-modal search but cannot interleave modalities, and generative assistants, which support region-level interpretation but lack scalable retrieval capabilities. We propose $\textbf{VLM2GeoVec}$, an instruction-following, single-encoder vision-language model trained contrastively to embed interleaved inputs (images, text, bounding boxes, and geographic coordinates) in a unified vector space. Our single encoder interleaves all inputs into one joint embedding trained with a contrastive loss, eliminating multi-stage pipelines and task-specific modules. To evaluate its versatility, we introduce $\textbf{RSMEB}$, a novel benchmark covering key remote-sensing embedding applications: scene classification; cross-modal search; compositional retrieval; visual-question answering; visual grounding and region-level reasoning; and semantic geospatial retrieval. On RSMEB, it achieves $\textbf{26.6%}$ P@1 on region-caption retrieval (+25 pp vs. dual-encoder baselines), $\textbf{32.5%}$ P@1 on referring-expression retrieval (+19 pp), and $\textbf{17.8%}$ P@1 on semantic geo-localization retrieval (over $3\times$ prior best), while matching or exceeding specialized baselines on conventional tasks such as scene classification and cross-modal retrieval. VLM2GeoVec unifies scalable retrieval with region-level spatial reasoning, enabling cohesive multimodal analysis in remote sensing. We will publicly release the code, checkpoints, and data upon acceptance.

