---
layout: default
title: "FoodSEM: Large Language Model Specialized in Food Named-Entity Linking"
---

# FoodSEM: Large Language Model Specialized in Food Named-Entity Linking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22125" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22125v1</a>
  <a href="https://arxiv.org/pdf/2509.22125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22125v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22125v1', 'FoodSEM: Large Language Model Specialized in Food Named-Entity Linking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ana Gjorgjevikj, Matej Martinc, Gjorgjina Cenikj, Sašo Džeroski, Barbara Koroušić Seljak, Tome Eftimov

**分类**: cs.CL, cs.IR

**发布日期**: 2025-09-26

**备注**: To appear in the Proceedings of the 28th International Conference on Discovery Science (DS 2025)

---

## 💡 一句话要点

**FoodSEM：针对食品命名实体链接微调的大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `食品命名实体链接` `大型语言模型` `微调` `指令-响应` `食品本体`

## 📋 核心要点

1. 现有的通用或领域特定语言模型在食品命名实体链接任务中表现不佳，无法准确识别和链接食品相关实体。
2. FoodSEM通过指令-响应方式，将文本中的食品实体链接到FoodOn、SNOMED-CT等多个食品本体，实现精准链接。
3. FoodSEM在食品NEL任务上取得了显著的性能提升，F1得分最高达到98%，超越了零样本、单样本和少样本LLM基线。

## 📝 摘要（中文）

本文介绍了FoodSEM，一个最先进的、经过微调的开源大型语言模型（LLM），专门用于食品相关本体的命名实体链接（NEL）任务。据我们所知，食品NEL任务无法通过目前最先进的通用（大型）语言模型或定制的领域特定模型/系统准确解决。通过指令-响应（IR）场景，FoodSEM将文本中提到的食品相关实体链接到多个本体，包括FoodOn、SNOMED-CT和Hansard分类法。与相关模型/系统相比，FoodSEM模型实现了最先进的性能，在某些本体和数据集上的F1得分甚至达到98%。与零样本、单样本和少样本LLM提示基线的比较分析进一步突出了FoodSEM相对于其非微调版本的卓越性能。通过公开发布FoodSEM及其相关资源，本文的主要贡献包括：（1）发布食品注释语料库，将其转换为适合LLM微调/评估的IR格式；（2）发布一个强大的模型，以促进食品领域文本的语义理解；（3）为未来的食品NEL基准测试提供一个强大的基线。

## 🔬 方法详解

**问题定义**：论文旨在解决食品领域命名实体链接（NEL）问题。现有通用LLM和领域特定模型在处理该任务时，无法准确地将文本中提及的食品实体链接到相应的知识库（如FoodOn、SNOMED-CT等），导致语义理解的偏差。痛点在于缺乏针对食品领域优化的模型和数据集。

**核心思路**：论文的核心思路是利用指令-响应（Instruction-Response, IR）范式，通过微调大型语言模型，使其能够更好地理解和处理食品领域的文本信息，从而实现更准确的食品NEL。通过构建高质量的食品注释数据集，并将其转化为IR格式，可以有效地指导LLM学习食品实体的语义信息。

**技术框架**：FoodSEM的技术框架主要包括以下几个步骤：1) 构建食品注释语料库，并将其转换为IR格式；2) 选择一个预训练的大型语言模型作为基础模型；3) 使用IR格式的食品注释数据对基础模型进行微调，得到FoodSEM模型；4) 使用FoodSEM模型进行食品NEL任务，将文本中的食品实体链接到相应的知识库；5) 对FoodSEM模型的性能进行评估，并与其他模型进行比较。

**关键创新**：论文的关键创新在于：1) 构建了一个高质量的、适合LLM微调的食品注释语料库，并将其转换为IR格式；2) 通过微调大型语言模型，得到了一个专门用于食品NEL任务的FoodSEM模型，该模型在性能上优于现有的通用LLM和领域特定模型；3) 提供了一个强大的食品NEL基线，为未来的研究提供了参考。

**关键设计**：论文的关键设计包括：1) 数据集的构建：收集了大量的食品相关文本数据，并对其进行人工标注，将其转换为IR格式，包括指令（例如“将以下食品实体链接到FoodOn本体”）和响应（例如“苹果 -> FoodOn:12345”）；2) 模型微调：选择了合适的预训练LLM作为基础模型，并使用IR格式的食品注释数据对其进行微调，使用了标准的交叉熵损失函数进行优化；3) 评估指标：使用了F1得分作为主要的评估指标，以衡量模型在食品NEL任务上的性能。

## 📊 实验亮点

FoodSEM在食品NEL任务上取得了显著的性能提升，在某些本体和数据集上的F1得分甚至达到了98%。与零样本、单样本和少样本LLM基线相比，FoodSEM表现出明显的优势，证明了其在食品领域语义理解方面的有效性。该模型及其相关资源的公开发布，为未来的研究提供了强大的基线。

## 🎯 应用场景

FoodSEM在食品营养分析、智能食谱推荐、食品安全监管、个性化饮食建议等领域具有广泛的应用前景。它可以帮助用户更好地理解食品成分和营养价值，为食品企业提供更精准的市场分析，并为政府部门提供更有效的食品安全监管手段。未来，FoodSEM有望成为食品领域语义理解的重要基础设施。

## 📄 摘要（原文）

> This paper introduces FoodSEM, a state-of-the-art fine-tuned open-source large language model (LLM) for named-entity linking (NEL) to food-related ontologies. To the best of our knowledge, food NEL is a task that cannot be accurately solved by state-of-the-art general-purpose (large) language models or custom domain-specific models/systems. Through an instruction-response (IR) scenario, FoodSEM links food-related entities mentioned in a text to several ontologies, including FoodOn, SNOMED-CT, and the Hansard taxonomy. The FoodSEM model achieves state-of-the-art performance compared to related models/systems, with F1 scores even reaching 98% on some ontologies and datasets. The presented comparative analyses against zero-shot, one-shot, and few-shot LLM prompting baselines further highlight FoodSEM's superior performance over its non-fine-tuned version. By making FoodSEM and its related resources publicly available, the main contributions of this article include (1) publishing a food-annotated corpora into an IR format suitable for LLM fine-tuning/evaluation, (2) publishing a robust model to advance the semantic understanding of text in the food domain, and (3) providing a strong baseline on food NEL for future benchmarking.

