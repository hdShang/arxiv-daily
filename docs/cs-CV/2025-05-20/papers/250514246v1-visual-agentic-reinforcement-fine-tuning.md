---
layout: default
title: Visual Agentic Reinforcement Fine-Tuning
---

# Visual Agentic Reinforcement Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14246" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14246v1</a>
  <a href="https://arxiv.org/pdf/2505.14246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14246v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14246v1', 'Visual Agentic Reinforcement Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyu Liu, Yuhang Zang, Yushan Zou, Zijian Liang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, Jiaqi Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-20

**备注**: project url: https://github.com/Liuziyu77/Visual-RFT/tree/main/Visual-ARFT

---

## 💡 一句话要点

**提出视觉代理强化微调方法以提升多模态推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉代理` `强化学习` `多模态推理` `图像处理` `信息检索` `大型语言模型` `开源研究`

## 📋 核心要点

1. 现有方法在多模态代理能力方面的研究相对不足，缺乏有效的基准和评估手段。
2. 本研究提出视觉代理强化微调（Visual-ARFT），使LVLMs具备实时信息获取和图像处理能力。
3. 实验结果显示，Visual-ARFT在多个基准测试中显著提升了模型性能，超越了现有的最先进模型。

## 📝 摘要（中文）

在大型推理模型（如OpenAI的o3）中，原生的代理能力使其能够使用外部工具进行搜索和代码执行，从而实现图像思考。尽管在语言代理能力方面已有显著进展，但多模态代理能力的发展仍较少探索。本研究提出视觉代理强化微调（Visual-ARFT），有效提升大型视觉语言模型（LVLMs）的灵活推理能力。通过Visual-ARFT，开源LVLMs能够实时浏览网站获取信息，并通过代码对输入图像进行处理和分析。我们还设计了多模态代理工具基准（MAT），用于评估LVLMs的搜索和编码能力。实验结果表明，Visual-ARFT在MAT-Coding和MAT-Search上分别比基线提升了+18.6% F1和+10.3% F1，超越了GPT-4o，并在多跳问答基准上也表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型视觉语言模型在多模态代理能力方面的不足，尤其是在实时信息获取和图像处理能力的缺乏。现有方法主要集中于语言代理能力，未能有效整合图像思考能力。

**核心思路**：论文提出的Visual-ARFT方法通过强化学习的方式，结合视觉信息与语言模型，提升模型的灵活性和适应性，使其能够在多模态环境中进行有效推理。

**技术框架**：整体架构包括两个主要模块：信息检索模块和图像处理模块。信息检索模块负责实时获取网页信息，而图像处理模块则通过编写代码实现对输入图像的操作，如裁剪和旋转。

**关键创新**：Visual-ARFT的核心创新在于将视觉信息与语言模型的代理能力结合，形成一种新的多模态推理机制。这种设计使得模型不仅能够理解文本，还能有效处理图像信息，显著提升了推理能力。

**关键设计**：在模型训练中，采用了特定的损失函数来平衡语言和视觉信息的学习，同时设置了多种超参数以优化模型在不同任务上的表现。

## 📊 实验亮点

实验结果显示，Visual-ARFT在MAT-Coding和MAT-Search基准上分别提升了+18.6% F1和+10.3% F1，超越了GPT-4o。此外，在多跳问答基准如2Wiki和HotpotQA上，Visual-ARFT也实现了+29.3% F1和+25.9% EM的显著提升，展示了其强大的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化内容生成、图像分析和多模态搜索引擎等。通过提升模型的多模态推理能力，能够在更复杂的任务中提供更准确和灵活的解决方案，推动人工智能在实际应用中的发展。

## 📄 摘要（原文）

> A key trend in Large Reasoning Models (e.g., OpenAI's o3) is the native agentic ability to use external tools such as web browsers for searching and writing/executing code for image manipulation to think with images. In the open-source research community, while significant progress has been made in language-only agentic abilities such as function calling and tool integration, the development of multi-modal agentic capabilities that involve truly thinking with images, and their corresponding benchmarks, are still less explored. This work highlights the effectiveness of Visual Agentic Reinforcement Fine-Tuning (Visual-ARFT) for enabling flexible and adaptive reasoning abilities for Large Vision-Language Models (LVLMs). With Visual-ARFT, open-source LVLMs gain the ability to browse websites for real-time information updates and write code to manipulate and analyze input images through cropping, rotation, and other image processing techniques. We also present a Multi-modal Agentic Tool Bench (MAT) with two settings (MAT-Search and MAT-Coding) designed to evaluate LVLMs' agentic search and coding abilities. Our experimental results demonstrate that Visual-ARFT outperforms its baseline by +18.6% F1 / +13.0% EM on MAT-Coding and +10.3% F1 / +8.7% EM on MAT-Search, ultimately surpassing GPT-4o. Visual-ARFT also achieves +29.3 F1% / +25.9% EM gains on existing multi-hop QA benchmarks such as 2Wiki and HotpotQA, demonstrating strong generalization capabilities. Our findings suggest that Visual-ARFT offers a promising path toward building robust and generalizable multimodal agents.

