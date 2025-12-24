---
layout: default
title: Decoding Neighborhood Environments with Large Language Models
---

# Decoding Neighborhood Environments with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08163" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08163v1</a>
  <a href="https://arxiv.org/pdf/2505.08163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08163v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08163v1', 'Decoding Neighborhood Environments with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Cart, Shaohu Zhang, Melanie Escue, Xugui Zhou, Haitao Zhao, Prashanth BusiReddyGari, Beiyu Lin, Shuang Li

**分类**: cs.AI, cs.CV

**发布日期**: 2025-05-13

**备注**: 8 pages

---

## 💡 一句话要点

**利用大型语言模型解码邻里环境以提升健康评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `邻里环境` `大型语言模型` `YOLOv11` `环境指标` `自动化评估` `公共卫生` `城市规划`

## 📋 核心要点

1. 现有评估邻里环境的方法如实地调查和GIS，资源消耗大且难以大规模实施。
2. 本研究提出利用大型语言模型（LLMs）解码邻里环境，降低人工标注需求，提升评估效率。
3. 通过训练YOLOv11模型和评估多个LLM，最终实现超过88%的准确率，展示了LLMs的潜力。

## 📝 摘要（中文）

邻里环境包括住房质量、道路和人行道等物理和环境条件，这些因素显著影响人类健康和福祉。传统的评估方法，如实地调查和地理信息系统（GIS），资源密集且难以大规模评估。尽管机器学习提供了自动化分析的潜力，但标注训练数据的繁琐过程和缺乏可访问模型限制了其可扩展性。本研究探讨了大型语言模型（LLMs）如ChatGPT和Gemini在大规模解码邻里环境（如人行道和电线）中的可行性。我们训练了一个基于YOLOv11的模型，在检测六个环境指标（包括路灯、人行道、电线、公寓、单车道和多车道）时，平均准确率达到99.13%。随后，我们评估了包括ChatGPT、Gemini、Claude和Grok在内的四个LLM，以评估它们识别这些指标的可行性、稳健性和局限性，重点关注提示策略和微调的影响。通过对前三个LLM进行多数投票，我们实现了超过88%的准确率，证明LLMs可以成为解码邻里环境的有用工具，无需任何训练努力。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统邻里环境评估方法的资源密集性和可扩展性不足的问题。现有方法如实地调查和GIS难以在大规模上进行有效评估。

**核心思路**：论文提出利用大型语言模型（LLMs）来解码邻里环境，尤其是通过自动化手段识别环境指标，减少对人工标注的依赖。

**技术框架**：整体架构包括两个主要模块：首先是基于YOLOv11的模型用于检测环境指标，其次是评估多个LLM在识别这些指标中的表现。

**关键创新**：最重要的创新点在于将LLMs应用于环境指标的解码，尤其是通过多数投票策略提升识别准确性，与传统方法相比显著降低了人工干预。

**关键设计**：在模型训练中，YOLOv11的网络结构经过优化，采用特定的损失函数以提高检测精度，同时在LLM的评估中，设计了不同的提示策略和微调方法以增强模型的识别能力。

## 📊 实验亮点

实验结果显示，YOLOv11模型在检测六个环境指标时，平均准确率达到99.13%。通过对前三个LLM进行多数投票，最终实现超过88%的准确率，表明LLMs在解码邻里环境中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、公共卫生和环境监测等。通过利用大型语言模型，能够在更大范围内快速评估邻里环境，进而为政策制定和社区发展提供数据支持，提升人们的生活质量。

## 📄 摘要（原文）

> Neighborhood environments include physical and environmental conditions such as housing quality, roads, and sidewalks, which significantly influence human health and well-being. Traditional methods for assessing these environments, including field surveys and geographic information systems (GIS), are resource-intensive and challenging to evaluate neighborhood environments at scale. Although machine learning offers potential for automated analysis, the laborious process of labeling training data and the lack of accessible models hinder scalability. This study explores the feasibility of large language models (LLMs) such as ChatGPT and Gemini as tools for decoding neighborhood environments (e.g., sidewalk and powerline) at scale. We train a robust YOLOv11-based model, which achieves an average accuracy of 99.13% in detecting six environmental indicators, including streetlight, sidewalk, powerline, apartment, single-lane road, and multilane road. We then evaluate four LLMs, including ChatGPT, Gemini, Claude, and Grok, to assess their feasibility, robustness, and limitations in identifying these indicators, with a focus on the impact of prompting strategies and fine-tuning. We apply majority voting with the top three LLMs to achieve over 88% accuracy, which demonstrates LLMs could be a useful tool to decode the neighborhood environment without any training effort.

