---
layout: default
title: HideAndSeg: an AI-based tool with automated prompting for octopus segmentation in natural habitats
---

# HideAndSeg: an AI-based tool with automated prompting for octopus segmentation in natural habitats

**arXiv**: [2511.04426v1](https://arxiv.org/abs/2511.04426) | [PDF](https://arxiv.org/pdf/2511.04426.pdf)

**作者**: Alan de Aguiar, Michaella Pereira Andrade, Charles Morphy D. Santos, João Paulo Gois

---

## 💡 一句话要点

**提出HideAndSeg工具，通过自动化提示实现自然栖息地章鱼视频分割**

**关键词**: `视频分割` `无监督评估` `SAM2集成` `YOLO检测` `章鱼行为研究`

## 📋 核心要点

1. 核心问题：章鱼伪装、变形和遮挡导致自然栖息地视频分割困难，缺乏大规模标注数据。
2. 方法要点：集成SAM2和YOLOv11，先手动点提示生成掩码，后自动边界框提示实现全流程自动化。
3. 实验或效果：引入无监督指标评估分割质量，减少噪声，在完全遮挡后仍能重识别和分割章鱼。

## 📄 摘要（原文）

> Analyzing octopuses in their natural habitats is challenging due to their
> camouflage capability, rapid changes in skin texture and color, non-rigid body
> deformations, and frequent occlusions, all of which are compounded by variable
> underwater lighting and turbidity. Addressing the lack of large-scale annotated
> datasets, this paper introduces HideAndSeg, a novel, minimally supervised
> AI-based tool for segmenting videos of octopuses. It establishes a quantitative
> baseline for this task. HideAndSeg integrates SAM2 with a custom-trained
> YOLOv11 object detector. First, the user provides point coordinates to generate
> the initial segmentation masks with SAM2. These masks serve as training data
> for the YOLO model. After that, our approach fully automates the pipeline by
> providing a bounding box prompt to SAM2, eliminating the need for further
> manual intervention. We introduce two unsupervised metrics - temporal
> consistency $DICE_t$ and new component count $NC_t$ - to quantitatively
> evaluate segmentation quality and guide mask refinement in the absence of
> ground-truth data, i.e., real-world information that serves to train, validate,
> and test AI models. Results show that HideAndSeg achieves satisfactory
> performance, reducing segmentation noise compared to the manually prompted
> approach. Our method can re-identify and segment the octopus even after periods
> of complete occlusion in natural environments, a scenario in which the manually
> prompted model fails. By reducing the need for manual analysis in real-world
> scenarios, this work provides a practical tool that paves the way for more
> efficient behavioral studies of wild cephalopods.

