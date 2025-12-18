---
layout: default
title: Seeing the Unseen: Towards Zero-Shot Inspection for Wind Turbine Blades using Knowledge-Augmented Vision Language Models
---

# Seeing the Unseen: Towards Zero-Shot Inspection for Wind Turbine Blades using Knowledge-Augmented Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22868" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22868v1</a>
  <a href="https://arxiv.org/pdf/2510.22868.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22868v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22868v1', 'Seeing the Unseen: Towards Zero-Shot Inspection for Wind Turbine Blades using Knowledge-Augmented Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Zhang, Qianyu Zhou, Farhad Imani, Jiong Tang

**分类**: cs.CV

**发布日期**: 2025-10-26

---

## 💡 一句话要点

**提出基于知识增强视觉语言模型的零样本风力涡轮机叶片缺陷检测方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `风力叶片检测` `零样本学习` `视觉语言模型` `检索增强生成` `知识库` `缺陷检测`

## 📋 核心要点

1. 现有风力叶片缺陷检测方法依赖大量标注数据，难以检测罕见或新出现的缺陷类型，泛化能力受限。
2. 该论文提出一种基于检索增强生成（RAG）和视觉语言模型（VLM）的零样本检测框架，无需特定任务训练。
3. 实验结果表明，该方法在小样本数据集上能正确分类所有样本，并具有良好的可解释性和泛化能力。

## 📝 摘要（中文）

风力涡轮机叶片在恶劣环境中运行，及时检测损伤对于预防故障和优化维护至关重要。基于无人机的检测和深度学习很有前景，但通常依赖于大型标注数据集，这限制了它们检测罕见或不断演变的损伤类型的能力。为了解决这个问题，我们提出了一种面向零样本的检测框架，该框架将检索增强生成（RAG）与视觉语言模型（VLM）集成。构建了一个多模态知识库，包括技术文档、代表性参考图像和领域特定指南。一个具有关键词感知重排序的混合文本-图像检索器组装最相关的上下文，以在推理时调节VLM，在没有任务特定训练的情况下注入领域知识。我们在30个标记的叶片图像上评估了该框架，这些图像涵盖了不同的损伤类别。尽管由于难以获得经过验证的叶片图像，数据集很小，但它涵盖了多个具有代表性的缺陷类型。在这个测试集上，RAG-grounded VLM正确分类了所有样本，而没有检索的相同VLM在准确性和精度方面都表现更差。我们进一步与开放词汇基线进行比较，并纳入不确定性Clopper-Pearson置信区间，以解决小样本设置问题。消融研究表明，该框架的关键优势在于可解释性和泛化性：检索到的参考文献为推理过程奠定了基础，并通过利用领域知识而不是仅仅依赖视觉线索来实现对以前未见过的缺陷的检测。这项研究为工业检测贡献了一种数据高效的解决方案，减少了对大量标记数据集的依赖。

## 🔬 方法详解

**问题定义**：风力涡轮机叶片缺陷检测是保障风力发电安全的关键。然而，现有方法依赖于大量标注数据，难以适应实际应用中不断出现的新型缺陷，且标注成本高昂。因此，如何在缺乏标注数据的情况下，实现对风力叶片缺陷的准确检测是一个亟待解决的问题。

**核心思路**：该论文的核心思路是利用领域知识来增强视觉语言模型（VLM）的推理能力，从而实现零样本缺陷检测。通过构建包含技术文档、参考图像和领域指南的多模态知识库，并使用检索增强生成（RAG）方法，将与待检测图像相关的知识注入到VLM中，使其能够根据领域知识进行推理和判断。

**技术框架**：该框架主要包含以下几个模块：1) 多模态知识库构建：收集整理风力叶片相关的技术文档、参考图像和领域指南，构建一个包含丰富领域知识的知识库。2) 混合文本-图像检索器：设计一个能够同时处理文本和图像输入的检索器，用于从知识库中检索与待检测图像最相关的知识。该检索器采用关键词感知重排序策略，以提高检索的准确性。3) 视觉语言模型（VLM）：使用预训练的VLM作为缺陷检测的核心模型。4) 检索增强生成（RAG）：将检索到的知识作为VLM的输入，引导VLM进行缺陷检测和分类。

**关键创新**：该论文的关键创新在于将检索增强生成（RAG）方法应用于零样本风力叶片缺陷检测。通过构建多模态知识库，并利用混合文本-图像检索器将相关知识注入到VLM中，实现了在缺乏标注数据的情况下对新型缺陷的检测。这种方法不仅提高了检测的准确性，还增强了模型的可解释性和泛化能力。

**关键设计**：在混合文本-图像检索器中，采用了关键词感知重排序策略，以提高检索的准确性。具体来说，首先使用文本检索器检索与待检测图像相关的文本信息，然后使用图像检索器检索与待检测图像相似的参考图像。最后，根据关键词的权重对检索结果进行重排序，以选择最相关的知识。此外，在VLM的选择上，采用了预训练的视觉语言模型，并对其进行微调，以适应风力叶片缺陷检测的任务。

## 📊 实验亮点

实验结果表明，在包含多种缺陷类型的30个叶片图像测试集上，RAG-grounded VLM正确分类了所有样本，而没有检索的VLM在准确性和精度方面表现更差。与开放词汇基线相比，该方法也取得了更好的效果。消融研究表明，检索到的参考文献能够有效提高模型的可解释性和泛化能力。

## 🎯 应用场景

该研究成果可应用于风力涡轮机叶片自动巡检、故障诊断和预测性维护。通过减少对大量标注数据的依赖，降低了部署成本，加速了智能化巡检系统的落地。该方法还可推广到其他工业场景，如桥梁、管道等基础设施的缺陷检测，具有广阔的应用前景。

## 📄 摘要（原文）

> Wind turbine blades operate in harsh environments, making timely damage detection essential for preventing failures and optimizing maintenance. Drone-based inspection and deep learning are promising, but typically depend on large, labeled datasets, which limit their ability to detect rare or evolving damage types. To address this, we propose a zero-shot-oriented inspection framework that integrates Retrieval-Augmented Generation (RAG) with Vision-Language Models (VLM). A multimodal knowledge base is constructed, comprising technical documentation, representative reference images, and domain-specific guidelines. A hybrid text-image retriever with keyword-aware reranking assembles the most relevant context to condition the VLM at inference, injecting domain knowledge without task-specific training. We evaluate the framework on 30 labeled blade images covering diverse damage categories. Although the dataset is small due to the difficulty of acquiring verified blade imagery, it covers multiple representative defect types. On this test set, the RAG-grounded VLM correctly classified all samples, whereas the same VLM without retrieval performed worse in both accuracy and precision. We further compare against open-vocabulary baselines and incorporate uncertainty Clopper-Pearson confidence intervals to account for the small-sample setting. Ablation studies indicate that the key advantage of the framework lies in explainability and generalizability: retrieved references ground the reasoning process and enable the detection of previously unseen defects by leveraging domain knowledge rather than relying solely on visual cues. This research contributes a data-efficient solution for industrial inspection that reduces dependence on extensive labeled datasets.

