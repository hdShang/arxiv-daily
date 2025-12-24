---
layout: default
title: "CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation"
---

# CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17324" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17324v2</a>
  <a href="https://arxiv.org/pdf/2508.17324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17324v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17324v2', 'CultranAI at PalmX 2025: Data Augmentation for Cultural Knowledge Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hunzalah Hassan Bhatti, Youssef Ahmed, Md Arid Hasan, Firoj Alam

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-24 (更新: 2025-10-01)

**备注**: LLMs, Native, Arabic LLMs, Augmentation, Multilingual, Language Diversity, Contextual Understanding, Minority Languages, Culturally Informed, Foundation Models, Large Language Models

---

## 💡 一句话要点

**提出CultranAI以增强阿拉伯文化知识表示**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据增强` `文化知识表示` `大语言模型` `LoRA微调` `多项选择题`

## 📋 核心要点

1. 现有方法在阿拉伯文化知识表示方面存在数据不足和模型性能不佳的挑战。
2. 论文提出通过数据增强和LoRA微调大语言模型，结合多个数据集以提升文化知识表示能力。
3. 实验结果显示，Fanar-1-9B-Instruct模型在增强数据集上表现优异，准确率显著提升。

## 📝 摘要（中文）

本文报告了我们在PalmX文化评估共享任务中的参与。我们的系统CultranAI专注于数据增强和大语言模型（LLMs）的LoRA微调，以实现阿拉伯文化知识的表示。我们基准测试了多个LLM，以确定在该任务中表现最佳的模型。除了利用PalmX数据集外，我们还通过整合Palm数据集来增强数据，并策划了一个包含超过22,000个文化基础的多项选择题（MCQs）的新数据集。实验表明，Fanar-1-9B-Instruct模型表现最佳。我们在结合增强数据集的基础上对该模型进行了微调。在盲测集上，我们提交的系统排名第5，准确率为70.50%；而在PalmX开发集上，准确率达到了84.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决阿拉伯文化知识表示中的数据稀缺和模型性能不足的问题。现有方法在处理文化知识时往往缺乏足够的多样性和准确性。

**核心思路**：论文的核心思路是通过数据增强和LoRA微调技术，结合多个数据集来提升大语言模型在文化知识表示上的能力。这样的设计旨在提高模型对文化内容的理解和生成能力。

**技术框架**：整体架构包括数据集的整合、数据增强、模型选择与微调几个主要模块。首先，整合PalmX和Palm数据集，然后创建新的多项选择题数据集，最后对选定的LLM进行微调。

**关键创新**：最重要的技术创新在于结合了多个数据集进行数据增强，并通过LoRA微调技术优化了大语言模型的性能。这种方法与传统的单一数据集训练方法有本质区别。

**关键设计**：在模型微调过程中，采用了Fanar-1-9B-Instruct模型，并设置了适当的学习率和损失函数，以确保模型在处理文化知识时的准确性和鲁棒性。

## 📊 实验亮点

实验结果显示，Fanar-1-9B-Instruct模型在盲测集上取得了70.50%的准确率，在PalmX开发集上达到了84.1%的准确率，表现优于其他基线模型，验证了数据增强和微调的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、文化传播和智能问答系统。通过增强的文化知识表示，系统能够更好地理解和生成与阿拉伯文化相关的内容，提升用户体验和学习效果。未来，该方法还可以扩展到其他文化背景的知识表示任务中。

## 📄 摘要（原文）

> In this paper, we report our participation to the PalmX cultural evaluation shared task. Our system, CultranAI, focused on data augmentation and LoRA fine-tuning of large language models (LLMs) for Arabic cultural knowledge representation. We benchmarked several LLMs to identify the best-performing model for the task. In addition to utilizing the PalmX dataset, we augmented it by incorporating the Palm dataset and curated a new dataset of over 22K culturally grounded multiple-choice questions (MCQs). Our experiments showed that the Fanar-1-9B-Instruct model achieved the highest performance. We fine-tuned this model on the combined augmented dataset of 22K+ MCQs. On the blind test set, our submitted system ranked 5th with an accuracy of 70.50%, while on the PalmX development set, it achieved an accuracy of 84.1%.

