---
layout: default
title: CrossMed: A Multimodal Cross-Task Benchmark for Compositional Generalization in Medical Imaging
---

# CrossMed: A Multimodal Cross-Task Benchmark for Compositional Generalization in Medical Imaging

**arXiv**: [2511.11034v1](https://arxiv.org/abs/2511.11034) | [PDF](https://arxiv.org/pdf/2511.11034.pdf)

**作者**: Pooja Singh, Siddhant Ujjain, Tapan Kumar Gandhi, Sandeep Kumar

---

## 💡 一句话要点

**提出CrossMed基准以评估医学多模态大模型在组合泛化中的表现**

**关键词**: `组合泛化` `医学多模态基准` `视觉问答` `多模态大语言模型` `零样本泛化` `跨任务迁移`

## 📋 核心要点

1. 核心问题：医学多模态大模型在未见模态-解剖-任务组合上的泛化能力不足
2. 方法要点：基于MAT框架统一四个公共数据集为视觉问答格式，构建20,200个多选问题
3. 实验或效果：模型在相关分割上表现良好，但在无关和零重叠条件下性能显著下降

## 📄 摘要（原文）

> Recent advances in multimodal large language models have enabled unified processing of visual and textual inputs, offering promising applications in general-purpose medical AI. However, their ability to generalize compositionally across unseen combinations of imaging modality, anatomy, and task type remains underexplored. We introduce CrossMed, a benchmark designed to evaluate compositional generalization (CG) in medical multimodal LLMs using a structured Modality-Anatomy-Task (MAT) schema. CrossMed reformulates four public datasets, CheXpert (X-ray classification), SIIM-ACR (X-ray segmentation), BraTS 2020 (MRI classification and segmentation), and MosMedData (CT classification) into a unified visual question answering (VQA) format, resulting in 20,200 multiple-choice QA instances. We evaluate two open-source multimodal LLMs, LLaVA-Vicuna-7B and Qwen2-VL-7B, on both Related and Unrelated MAT splits, as well as a zero-overlap setting where test triplets share no Modality, Anatomy, or Task with the training data. Models trained on Related splits achieve 83.2 percent classification accuracy and 0.75 segmentation cIoU, while performance drops significantly under Unrelated and zero-overlap conditions, demonstrating the benchmark difficulty. We also show cross-task transfer, where segmentation performance improves by 7 percent cIoU even when trained using classification-only data. Traditional models (ResNet-50 and U-Net) show modest gains, confirming the broad utility of the MAT framework, while multimodal LLMs uniquely excel at compositional generalization. CrossMed provides a rigorous testbed for evaluating zero-shot, cross-task, and modality-agnostic generalization in medical vision-language models.

