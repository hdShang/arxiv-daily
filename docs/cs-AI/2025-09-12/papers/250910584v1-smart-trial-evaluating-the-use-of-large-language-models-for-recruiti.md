---
layout: default
title: "Smart Trial: Evaluating the Use of Large Language Models for Recruiting Clinical Trial Participants via Social Media"
---

# Smart Trial: Evaluating the Use of Large Language Models for Recruiting Clinical Trial Participants via Social Media

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10584" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10584v1</a>
  <a href="https://arxiv.org/pdf/2509.10584.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10584v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10584v1', 'Smart Trial: Evaluating the Use of Large Language Models for Recruiting Clinical Trial Participants via Social Media')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaofan Zhou, Zisu Wang, Janice Krieger, Mohan Zalake, Lu Cheng

**分类**: cs.CY, cs.AI, cs.CL

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**利用大型语言模型进行社交媒体临床试验招募：提出TRIALQA数据集并进行基准测试。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `临床试验招募` `大型语言模型` `社交媒体分析` `自然语言处理` `TRIALQA数据集`

## 📋 核心要点

1. 临床试验招募面临参与者资格标准复杂、传统方法耗时且受限的挑战。
2. 论文提出利用大型语言模型分析社交媒体数据，识别潜在的临床试验参与者。
3. 构建了TRIALQA数据集，包含结肠癌和前列腺癌相关的社交媒体数据，并对多种LLM进行了基准测试。

## 📝 摘要（中文）

临床试验（CT）对于推动医学研究和治疗至关重要，但高效招募符合条件的参与者仍然是一个重大挑战，因为每个参与者都必须满足复杂的资格标准。传统招募方法（如广告或医院内的电子健康记录筛选）通常耗时且受地理位置限制。本文通过利用个人在社交媒体平台上分享的大量健康相关信息来解决招募挑战。随着能够进行复杂文本理解的强大大型语言模型（LLM）的出现，我们提出了核心研究问题：LLM驱动的工具能否通过识别社交媒体上的潜在参与者来促进CT招募？为了研究这个问题，我们引入了TRIALQA，这是一个新颖的数据集，包含来自结肠癌和前列腺癌subreddit的两个社交媒体集合。使用来自公共真实CT的资格标准，聘请经验丰富的注释员来注释TRIALQA，以表明（1）社交媒体用户是否符合给定的资格标准，以及（2）用户参与CT的理由。我们使用六种不同的训练和推理策略，对这两种预测任务中的七种广泛使用的LLM进行了基准测试。我们广泛的实验表明，虽然LLM显示出相当大的希望，但它们在执行准确评估资格标准所需的复杂多跳推理方面仍然面临挑战。

## 🔬 方法详解

**问题定义**：论文旨在解决临床试验招募中，传统方法效率低下、难以触达潜在参与者的问题。现有方法依赖于广告或电子健康记录筛选，耗时且受地理位置限制，无法有效利用社交媒体上用户分享的大量健康信息。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的文本理解能力，分析社交媒体用户的发帖内容，判断其是否符合特定临床试验的资格标准。通过这种方式，可以更高效、更广泛地识别潜在的临床试验参与者。

**技术框架**：论文构建了一个名为TRIALQA的数据集，包含来自Reddit上结肠癌和前列腺癌子版块的社交媒体帖子。然后，使用真实临床试验的资格标准，由专业注释员对这些帖子进行标注，判断用户是否符合资格，并记录用户参与临床试验的理由。最后，使用不同的训练和推理策略，对七种广泛使用的LLM进行基准测试。

**关键创新**：论文的关键创新在于将大型语言模型应用于临床试验招募领域，并提出了TRIALQA数据集，为该领域的研究提供了数据基础。此外，论文还系统地评估了不同LLM在这一任务上的表现，并分析了其存在的挑战。

**关键设计**：论文使用了来自真实临床试验的资格标准进行标注，保证了标注的准确性和实用性。同时，论文采用了多种训练和推理策略，以评估不同LLM的性能。具体的LLM包括（具体模型名称未知），训练策略包括（具体训练策略未知），损失函数和网络结构等细节未在摘要中提及，属于未知信息。

## 📊 实验亮点

论文构建了包含结肠癌和前列腺癌subreddit数据的TRIALQA数据集，并对七种LLM进行了基准测试。实验结果表明，虽然LLM在临床试验招募方面展现出潜力，但在进行复杂的多跳推理以准确评估资格标准方面仍面临挑战。具体的性能数据和提升幅度在摘要中未明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于临床试验招募，提高招募效率，扩大招募范围，降低招募成本。通过分析社交媒体数据，可以更精准地定位潜在参与者，加速临床试验进程，推动医学研究发展。未来，该方法还可扩展到其他疾病领域，甚至用于公共卫生事件的监测和预警。

## 📄 摘要（原文）

> Clinical trials (CT) are essential for advancing medical research and treatment, yet efficiently recruiting eligible participants -- each of whom must meet complex eligibility criteria -- remains a significant challenge. Traditional recruitment approaches, such as advertisements or electronic health record screening within hospitals, are often time-consuming and geographically constrained. This work addresses the recruitment challenge by leveraging the vast amount of health-related information individuals share on social media platforms. With the emergence of powerful large language models (LLMs) capable of sophisticated text understanding, we pose the central research question: Can LLM-driven tools facilitate CT recruitment by identifying potential participants through their engagement on social media? To investigate this question, we introduce TRIALQA, a novel dataset comprising two social media collections from the subreddits on colon cancer and prostate cancer. Using eligibility criteria from public real-world CTs, experienced annotators are hired to annotate TRIALQA to indicate (1) whether a social media user meets a given eligibility criterion and (2) the user's stated reasons for interest in participating in CT. We benchmark seven widely used LLMs on these two prediction tasks, employing six distinct training and inference strategies. Our extensive experiments reveal that, while LLMs show considerable promise, they still face challenges in performing the complex, multi-hop reasoning needed to accurately assess eligibility criteria.

