---
layout: default
title: "LMOD+: A Comprehensive Multimodal Dataset and Benchmark for Developing and Evaluating Multimodal Large Language Models in Ophthalmology"
---

# LMOD+: A Comprehensive Multimodal Dataset and Benchmark for Developing and Evaluating Multimodal Large Language Models in Ophthalmology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25620" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25620v1</a>
  <a href="https://arxiv.org/pdf/2509.25620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25620v1', 'LMOD+: A Comprehensive Multimodal Dataset and Benchmark for Developing and Evaluating Multimodal Large Language Models in Ophthalmology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyue Qin, Yang Liu, Yu Yin, Jinyu Ding, Haoran Zhang, Anran Li, Dylan Campbell, Xuansheng Wu, Ke Zou, Tiarnan D. L. Keenan, Emily Y. Chew, Zhiyong Lu, Yih-Chung Tham, Ninghao Liu, Xiuzhen Zhang, Qingyu Chen

**分类**: cs.CV

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出LMOD+眼科多模态数据集与基准，用于评估多模态大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `眼科` `多模态学习` `大语言模型` `数据集` `疾病诊断` `图像分析` `人工智能`

## 📋 核心要点

1. 现有眼科多模态大语言模型缺乏全面评估基准，限制了其在疾病诊断和分期等任务上的发展。
2. 构建包含多种眼科疾病和成像模态的大规模数据集LMOD+，并进行多粒度标注，支持多种任务。
3. 系统评估了24个先进MLLM，揭示了其在眼科疾病筛查中的潜力，以及在复杂任务中的不足。

## 📝 摘要（中文）

本研究针对威胁视力的眼部疾病，由于专业人员短缺和医疗资源限制，及时诊断面临挑战。多模态大语言模型(MLLM)在医学图像解释方面展现潜力，但缺乏适用于评估生成模型的综合基准数据集阻碍了其在眼科领域的发展。为此，我们提出了一个大规模多模态眼科基准数据集LMOD+，包含32,633个实例，涵盖12种常见眼科疾病和5种成像方式，并具有多粒度标注。该数据集整合了图像、解剖结构、人口统计学和自由文本标注，支持解剖结构识别、疾病筛查、疾病分期和人口统计学预测以评估偏见。本工作扩展了先前的LMOD基准，主要改进包括：数据集扩大近50%，大幅增加了彩色眼底摄影；扩展了任务范围，包括二元疾病诊断、多类诊断、基于国际分级标准的严重程度分类和人口统计学预测；系统评估了24个最先进的MLLM。评估结果显示了MLLM的潜力和局限性。在零样本设置下，性能最佳的模型在疾病筛查中达到了约58%的准确率，但在疾病分期等具有挑战性的任务中，性能仍然欠佳。我们将公开发布数据集、管理流程和排行榜，以促进眼科人工智能应用，并减轻全球威胁视力的疾病负担。

## 🔬 方法详解

**问题定义**：现有眼科多模态大语言模型(MLLM)的开发和评估受到缺乏全面基准数据集的限制，尤其是在生成模型方面。现有方法难以有效评估MLLM在眼科疾病诊断、分期和偏见评估等方面的能力。

**核心思路**：本研究的核心思路是构建一个大规模、多模态、多粒度标注的眼科数据集LMOD+，以提供一个全面的基准，用于训练和评估MLLM在眼科领域的性能。通过整合多种成像模态、解剖结构、人口统计学信息和自由文本标注，LMOD+能够支持多种任务，包括疾病筛查、疾病分期、解剖结构识别和偏见评估。

**技术框架**：LMOD+数据集的构建流程包括数据收集、数据清洗、数据标注和数据整合四个主要阶段。数据收集阶段从多个来源收集眼科图像和相关临床数据。数据清洗阶段对收集到的数据进行预处理，包括图像质量评估、噪声去除和数据格式转换。数据标注阶段由专业的眼科医生对图像进行多粒度标注，包括疾病类型、疾病严重程度、解剖结构和自由文本描述。数据整合阶段将图像、标注和人口统计学信息整合到一个统一的数据集中。

**关键创新**：LMOD+的关键创新在于其数据集的规模、多样性和多粒度标注。与现有的眼科数据集相比，LMOD+包含更多的数据实例、更广泛的疾病类型和成像模态，以及更详细的标注信息。这种全面的数据集能够更好地支持MLLM的训练和评估，并促进眼科人工智能应用的发展。

**关键设计**：LMOD+数据集的关键设计包括：(1) 包含五种成像模态：彩色眼底摄影、光学相干断层扫描(OCT)、OCT血管造影(OCTA)、荧光素血管造影(FA)和吲哚菁绿血管造影(ICGA)；(2) 涵盖12种常见眼科疾病；(3) 提供多粒度标注，包括疾病类型、疾病严重程度、解剖结构和自由文本描述；(4) 包含人口统计学信息，用于评估偏见。

## 📊 实验亮点

在零样本设置下，最佳MLLM在LMOD+数据集的疾病筛查任务中达到了约58%的准确率。该结果表明MLLM在眼科疾病筛查方面具有潜力，但同时也揭示了其在疾病分期等复杂任务中仍存在局限性，未来仍有提升空间。

## 🎯 应用场景

该研究成果可应用于开发辅助眼科疾病诊断和管理的AI系统，例如：自动疾病筛查、疾病分期、治疗方案推荐等。通过部署在基层医疗机构或远程医疗平台，有望提高诊断效率，减少误诊率，并缓解眼科医生短缺的问题，最终改善患者的视觉健康。

## 📄 摘要（原文）

> Vision-threatening eye diseases pose a major global health burden, with timely diagnosis limited by workforce shortages and restricted access to specialized care. While multimodal large language models (MLLMs) show promise for medical image interpretation, advancing MLLMs for ophthalmology is hindered by the lack of comprehensive benchmark datasets suitable for evaluating generative models. We present a large-scale multimodal ophthalmology benchmark comprising 32,633 instances with multi-granular annotations across 12 common ophthalmic conditions and 5 imaging modalities. The dataset integrates imaging, anatomical structures, demographics, and free-text annotations, supporting anatomical structure recognition, disease screening, disease staging, and demographic prediction for bias evaluation. This work extends our preliminary LMOD benchmark with three major enhancements: (1) nearly 50% dataset expansion with substantial enlargement of color fundus photography; (2) broadened task coverage including binary disease diagnosis, multi-class diagnosis, severity classification with international grading standards, and demographic prediction; and (3) systematic evaluation of 24 state-of-the-art MLLMs. Our evaluations reveal both promise and limitations. Top-performing models achieved ~58% accuracy in disease screening under zero-shot settings, and performance remained suboptimal for challenging tasks like disease staging. We will publicly release the dataset, curation pipeline, and leaderboard to potentially advance ophthalmic AI applications and reduce the global burden of vision-threatening diseases.

