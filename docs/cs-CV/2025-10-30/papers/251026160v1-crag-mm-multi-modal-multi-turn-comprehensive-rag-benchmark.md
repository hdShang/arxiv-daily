---
layout: default
title: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark
---

# CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26160" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26160v1</a>
  <a href="https://arxiv.org/pdf/2510.26160.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26160v1" onclick="toggleFavorite(this, '2510.26160v1', 'CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Wang, Xiao Yang, Kai Sun, Parth Suresh, Sanat Sharma, Adam Czyzewski, Derek Andersen, Surya Appini, Arkav Banerjee, Sajal Choudhary, Shervin Ghasemlou, Ziqiang Guan, Akil Iyer, Haidar Khan, Lingkun Kong, Roy Luo, Tiffany Ma, Zhen Qiao, David Tran, Wenfang Xu, Skyler Yeatman, Chen Zhou, Gunveer Gujral, Yinglong Xia, Shane Moon, Nicolas Scheffer, Nirav Shah, Eun Chang, Yue Liu, Florian Metze, Tammy Stark, Zhaleh Feizollahi, Andrea Jessee, Mangesh Pujari, Ahmed Aly, Babak Damavandi, Rakesh Wanga, Anuj Kumar, Rohit Patel, Wen-tau Yih, Xin Luna Dong

**分类**: cs.CV

**发布日期**: 2025-10-30

---

## 💡 一句话要点

**提出CRAG-MM：一个用于可穿戴设备场景的多模态多轮对话RAG综合基准。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `多模态检索增强生成` `可穿戴设备` `多轮对话` `基准数据集` `图像质量` `知识图谱` `真实场景` `KDD Cup`

## 📋 核心要点

1. 现有MM-RAG基准在可穿戴设备场景下存在不足，无法全面评估多模态多轮对话的性能。
2. CRAG-MM通过构建包含真实场景图像和复杂问题的多模态数据集，填补了这一空白。
3. 实验表明，现有RAG方法在CRAG-MM上表现不佳，为未来的研究提供了明确的改进方向。

## 📝 摘要（中文）

本文提出了CRAG-MM，一个用于多模态多轮对话的综合RAG基准，尤其关注可穿戴设备场景。CRAG-MM包含6.5K个(图像，问题，答案)三元组和2K个基于视觉的多轮对话，覆盖13个领域，包括6.2K张模仿可穿戴设备拍摄的以自我为中心的图像。问题经过精心设计，反映了真实世界的场景和挑战，包括五种图像质量问题、六种问题类型、不同的实体流行度、不同的信息动态性和不同的对话轮数。设计了三个任务：单源增强、多源增强和多轮对话，每个任务都配有相关的检索语料库和API，用于图像-KG检索和网页检索。评估表明，直接的RAG方法在CRAG-MM单轮和多轮问答中的真实性分别仅为32%和43%，而最先进的行业解决方案具有相似的质量（32%/45%），表明仍有很大的改进空间。该基准已举办KDD Cup 2025，吸引了约1K参与者和5K提交，获胜解决方案将基线性能提高了28%，突显了其对推动该领域的早期影响。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态检索增强生成（MM-RAG）在可穿戴设备场景下的评测问题。现有方法缺乏针对该场景的综合基准，无法有效评估模型在处理真实世界复杂问题时的性能，尤其是在图像质量差、信息动态变化和多轮对话等挑战下。

**核心思路**：论文的核心思路是构建一个更贴近真实可穿戴设备使用场景的MM-RAG基准数据集CRAG-MM。通过精心设计的数据集，包含各种图像质量问题、问题类型、实体流行度、信息动态性和对话轮数，从而更全面地评估MM-RAG模型的性能。

**技术框架**：CRAG-MM基准包含以下几个关键组成部分：1) 多样化的数据集，包含6.5K个(图像，问题，答案)三元组和2K个多轮对话，覆盖13个领域；2) 6.2K张以自我为中心的图像，模拟可穿戴设备的拍摄效果；3) 三个任务：单源增强、多源增强和多轮对话；4) 相关的检索语料库和API，用于图像-KG检索和网页检索。

**关键创新**：CRAG-MM的关键创新在于其数据集的设计，它考虑了真实世界可穿戴设备场景下的各种挑战，例如图像质量问题（模糊、遮挡等）、问题类型多样性（识别、推理等）、实体流行度差异、信息动态变化以及多轮对话的复杂性。这使得CRAG-MM能够更全面地评估MM-RAG模型的性能。

**关键设计**：CRAG-MM的数据集构建过程中，对图像质量、问题类型、实体流行度、信息动态性和对话轮数进行了精细的控制。例如，通过模拟不同的拍摄条件来生成不同质量的图像，设计不同类型的问题来考察模型的推理能力，并引入知识图谱和网页检索来模拟信息动态变化。具体参数设置和损失函数取决于所使用的MM-RAG模型。

## 📊 实验亮点

实验结果表明，现有的RAG方法在CRAG-MM基准上的表现远未达到理想水平，单轮问答的真实性仅为32%，多轮问答为43%，即使是业界领先的解决方案也只有32%/45%。KDD Cup 2025的获胜方案将基线性能提高了28%，证明了CRAG-MM对推动该领域研究的积极作用。

## 🎯 应用场景

CRAG-MM基准的潜在应用领域包括智能眼镜、AR/VR助手等可穿戴设备。通过该基准，可以更好地评估和改进MM-RAG模型在这些设备上的性能，从而提升用户体验，例如提供更准确的物体识别、更自然的对话交互和更及时的信息检索。未来，该基准可以扩展到更多领域，例如智能家居、工业巡检等。

## 📄 摘要（原文）

> Wearable devices such as smart glasses are transforming the way people interact with their surroundings, enabling users to seek information regarding entities in their view. Multi-Modal Retrieval-Augmented Generation (MM-RAG) plays a key role in supporting such questions, yet there is still no comprehensive benchmark for this task, especially regarding wearables scenarios. To fill this gap, we present CRAG-MM -- a Comprehensive RAG benchmark for Multi-modal Multi-turn conversations. CRAG-MM contains a diverse set of 6.5K (image, question, answer) triplets and 2K visual-based multi-turn conversations across 13 domains, including 6.2K egocentric images designed to mimic captures from wearable devices. We carefully constructed the questions to reflect real-world scenarios and challenges, including five types of image-quality issues, six question types, varying entity popularity, differing information dynamism, and different conversation turns. We design three tasks: single-source augmentation, multi-source augmentation, and multi-turn conversations -- each paired with an associated retrieval corpus and APIs for both image-KG retrieval and webpage retrieval. Our evaluation shows that straightforward RAG approaches achieve only 32% and 43% truthfulness on CRAG-MM single- and multi-turn QA, respectively, whereas state-of-the-art industry solutions have similar quality (32%/45%), underscoring ample room for improvement. The benchmark has hosted KDD Cup 2025, attracting about 1K participants and 5K submissions, with winning solutions improving baseline performance by 28%, highlighting its early impact on advancing the field.

