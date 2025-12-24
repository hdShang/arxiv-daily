---
layout: default
title: "VisText-Mosquito: A Unified Multimodal Benchmark Dataset for Visual Detection, Segmentation, and Textual Reasoning on Mosquito Breeding Sites"
---

# VisText-Mosquito: A Unified Multimodal Benchmark Dataset for Visual Detection, Segmentation, and Textual Reasoning on Mosquito Breeding Sites

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14629" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14629v2</a>
  <a href="https://arxiv.org/pdf/2506.14629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14629v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14629v2', 'VisText-Mosquito: A Unified Multimodal Benchmark Dataset for Visual Detection, Segmentation, and Textual Reasoning on Mosquito Breeding Sites')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md. Adnanul Islam, Md. Faiyaz Abdullah Sayeedi, Md. Asaduzzaman Shuvo, Shahanur Rahman Bappy, Md Asiful Islam, Swakkhar Shatabda

**分类**: cs.CV, cs.CL

**发布日期**: 2025-06-17 (更新: 2025-09-20)

**🔗 代码/项目**: [GITHUB](https://github.com/adnanul-islam-jisun/VisText-Mosquito)

---

## 💡 一句话要点

**提出VisText-Mosquito以解决蚊虫滋生地检测与分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `蚊虫传播疾病` `多模态数据集` `目标检测` `图像分割` `自然语言推理` `公共卫生监测` `人工智能`

## 📋 核心要点

1. 蚊虫传播疾病的检测与控制面临着现有方法在自动化和准确性上的不足。
2. 提出的VisText-Mosquito数据集结合视觉与文本信息，支持蚊虫滋生地的检测、分割和推理。
3. 实验结果显示，YOLOv9s和YOLOv11n-Seg在目标检测和分割任务中均取得了显著的性能提升。

## 📝 摘要（中文）

蚊虫传播疾病对全球健康构成重大威胁，需早期检测和主动控制滋生地以防止疫情爆发。本文提出了VisText-Mosquito，一个多模态数据集，整合视觉和文本数据，支持蚊虫滋生地的自动检测、分割和推理分析。该数据集包含1828张用于目标检测的标注图像、142张水面分割图像及与每张图像关联的自然语言推理文本。YOLOv9s模型在目标检测中取得了最高精度0.92926和mAP@50为0.92891，而YOLOv11n-Seg在分割中达到精度0.91587和mAP@50为0.79795。经过测试，微调后的Mosquito-LLaMA3-8B模型在推理生成中表现最佳，最终损失为0.0028，BLEU分数为54.7，BERTScore为0.91，ROUGE-L为0.85。该数据集和模型框架强调“预防胜于治疗”的主题，展示了基于AI的检测如何主动应对蚊虫传播疾病的风险。数据集和实现代码已在GitHub上公开。

## 🔬 方法详解

**问题定义**：本研究旨在解决蚊虫滋生地的自动检测与分析问题。现有方法在处理视觉和文本信息的整合、自动化程度及准确性方面存在不足，难以有效应对蚊虫传播疾病的风险。

**核心思路**：论文提出的VisText-Mosquito数据集通过整合视觉数据和自然语言推理，提供了一个多模态的分析框架，旨在提高蚊虫滋生地的检测和分析能力。通过结合YOLO系列模型进行目标检测和分割，利用大规模视觉语言模型进行推理生成，形成了一个完整的解决方案。

**技术框架**：整体架构包括数据集构建、模型训练和推理生成三个主要模块。数据集包含标注图像和文本，模型训练使用YOLOv9s和YOLOv11n-Seg进行目标检测和分割，推理生成则采用Mosquito-LLaMA3-8B模型进行自然语言处理。

**关键创新**：最重要的技术创新在于提出了一个多模态数据集，结合视觉与文本信息，填补了现有研究在蚊虫滋生地分析中的空白。通过使用YOLO系列模型和大规模视觉语言模型，显著提升了检测和推理的准确性。

**关键设计**：在模型训练中，YOLOv9s和YOLOv11n-Seg的参数设置经过精细调整，损失函数设计考虑了目标检测和分割的特性，确保了模型在不同任务中的高效性和准确性。

## 📊 实验亮点

实验结果显示，YOLOv9s模型在目标检测任务中达到了最高精度0.92926，mAP@50为0.92891，而YOLOv11n-Seg在分割任务中取得了0.91587的精度和0.79795的mAP@50。微调后的Mosquito-LLaMA3-8B模型在推理生成中表现优异，最终损失为0.0028，BLEU分数为54.7，BERTScore为0.91，ROUGE-L为0.85，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括公共卫生监测、环境保护及智能城市建设等。通过自动化检测蚊虫滋生地，可以有效降低蚊虫传播疾病的风险，提升公共卫生管理的效率。未来，该研究成果有望推动更多基于AI的环境监测和疾病预防技术的发展。

## 📄 摘要（原文）

> Mosquito-borne diseases pose a major global health risk, requiring early detection and proactive control of breeding sites to prevent outbreaks. In this paper, we present VisText-Mosquito, a multimodal dataset that integrates visual and textual data to support automated detection, segmentation, and reasoning for mosquito breeding site analysis. The dataset includes 1,828 annotated images for object detection, 142 images for water surface segmentation, and natural language reasoning texts linked to each image. The YOLOv9s model achieves the highest precision of 0.92926 and mAP@50 of 0.92891 for object detection, while YOLOv11n-Seg reaches a segmentation precision of 0.91587 and mAP@50 of 0.79795. For reasoning generation, we tested a range of large vision-language models (LVLMs) in both zero-shot and few-shot settings. Our fine-tuned Mosquito-LLaMA3-8B model achieved the best results, with a final loss of 0.0028, a BLEU score of 54.7, BERTScore of 0.91, and ROUGE-L of 0.85. This dataset and model framework emphasize the theme "Prevention is Better than Cure", showcasing how AI-based detection can proactively address mosquito-borne disease risks. The dataset and implementation code are publicly available at GitHub: https://github.com/adnanul-islam-jisun/VisText-Mosquito

