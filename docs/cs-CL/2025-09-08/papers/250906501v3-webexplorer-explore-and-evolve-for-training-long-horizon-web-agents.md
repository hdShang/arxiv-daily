---
layout: default
title: "WebExplorer: Explore and Evolve for Training Long-Horizon Web Agents"
---

# WebExplorer: Explore and Evolve for Training Long-Horizon Web Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06501" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06501v3</a>
  <a href="https://arxiv.org/pdf/2509.06501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06501v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06501v3', 'WebExplorer: Explore and Evolve for Training Long-Horizon Web Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junteng Liu, Yunji Li, Chi Zhang, Jingyang Li, Aili Chen, Ke Ji, Weiyu Cheng, Zijia Wu, Chengyu Du, Qidi Xu, Jiayuan Song, Zhengmao Zhu, Wenhu Chen, Pengyu Zhao, Junxian He

**分类**: cs.CL

**发布日期**: 2025-09-08 (更新: 2025-09-26)

---

## 💡 一句话要点

**WebExplorer：通过探索和演化训练长程Web代理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Web代理` `信息搜寻` `长程推理` `数据生成` `强化学习`

## 📋 核心要点

1. 现有Web代理在复杂信息搜寻任务中表现不足，且缺乏透明性，主要原因是缺乏高质量、具有挑战性的训练数据。
2. WebExplorer通过模型驱动的探索和迭代式长短查询演化，系统地生成高质量、需要多步推理和复杂Web导航的查询-答案对。
3. WebExplorer-8B模型在多个信息搜寻基准测试中达到SOTA，并展现出强大的泛化能力，验证了该方法的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）的应用日益转向代理方向，其中Web浏览能力是从各种在线资源检索信息的基础。然而，现有的开源Web代理在复杂任务上的信息搜寻能力有限，或者缺乏透明的实现。本文指出，关键挑战在于缺乏具有挑战性的信息搜寻数据。为了解决这个限制，我们引入了WebExplorer：一种使用基于模型的探索和迭代的、由长到短的查询演化的系统数据生成方法。该方法创建了需要多步推理和复杂Web导航的具有挑战性的查询-答案对。通过利用我们精心策划的高质量数据集，我们成功地开发了先进的Web代理WebExplorer-8B，通过监督微调和强化学习。我们的模型支持128K上下文长度和高达100轮的工具调用，从而实现长程问题解决。在各种信息搜寻基准测试中，WebExplorer-8B在其规模上实现了最先进的性能。值得注意的是，作为一个8B大小的模型，WebExplorer-8B在RL训练后能够有效地搜索平均16轮，在BrowseComp-en/zh上实现了比WebSailor-72B更高的准确率，并在WebWalkerQA和FRAMES上获得了高达100B参数的模型中的最佳性能。除了这些信息搜寻任务之外，我们的模型还在HLE基准测试中实现了强大的泛化能力，即使它仅在知识密集型QA数据上进行训练。这些结果表明，我们的方法是通往长程Web代理的实用途径。

## 🔬 方法详解

**问题定义**：现有开源Web代理在处理复杂信息搜寻任务时能力有限，并且缺乏透明的实现细节。主要痛点在于缺乏足够数量和质量的、具有挑战性的训练数据，这些数据需要多步推理和复杂的Web导航才能解决。

**核心思路**：WebExplorer的核心思路是通过一种系统化的数据生成方法，即基于模型的探索和迭代式的长短查询演化，来创建高质量的、具有挑战性的查询-答案对。这种方法旨在模拟真实世界中用户在Web上进行复杂信息搜寻的过程，从而为Web代理提供更有效的训练数据。

**技术框架**：WebExplorer的数据生成流程主要包含两个阶段：探索阶段和演化阶段。在探索阶段，模型根据初始查询在Web上进行探索，收集相关信息。在演化阶段，模型根据收集到的信息，迭代地生成更精确、更短的查询，直到找到最终答案。然后，使用这些生成的查询-答案对来训练Web代理。

**关键创新**：WebExplorer的关键创新在于其数据生成方法，它能够自动生成高质量的、具有挑战性的Web信息搜寻数据。与以往依赖人工标注或简单规则生成数据的方法相比，WebExplorer能够更好地模拟真实世界中的信息搜寻过程，从而提高Web代理的性能。

**关键设计**：WebExplorer使用了大型语言模型作为其核心组件，用于查询生成、信息提取和决策制定。在训练WebExplorer-8B时，采用了监督微调和强化学习相结合的方法。监督微调用于初始化模型的参数，强化学习用于优化模型的长期决策能力，使其能够更好地完成长程信息搜寻任务。模型支持128K上下文长度和高达100轮的工具调用。

## 📊 实验亮点

WebExplorer-8B在多个信息搜寻基准测试中取得了显著成果。例如，在BrowseComp-en/zh上，WebExplorer-8B的准确率高于WebSailor-72B，尽管其模型规模远小于后者。在WebWalkerQA和FRAMES上，WebExplorer-8B也达到了高达100B参数的模型中的最佳性能。此外，该模型在HLE基准测试中也展现出强大的泛化能力。

## 🎯 应用场景

WebExplorer的研究成果可应用于各种需要Web信息搜寻的场景，例如智能助手、自动问答系统、知识图谱构建等。该研究有助于提升这些应用在处理复杂查询和长程推理任务时的性能，并为开发更智能、更高效的Web代理提供了一种可行的途径。未来，该技术有望在自动化知识获取、智能决策支持等领域发挥重要作用。

## 📄 摘要（原文）

> The paradigm of Large Language Models (LLMs) has increasingly shifted toward agentic applications, where web browsing capabilities are fundamental for retrieving information from diverse online sources. However, existing open-source web agents either demonstrate limited information-seeking abilities on complex tasks or lack transparent implementations. In this work, we identify that the key challenge lies in the scarcity of challenging data for information seeking. To address this limitation, we introduce WebExplorer: a systematic data generation approach using model-based exploration and iterative, long-to-short query evolution. This method creates challenging query-answer pairs that require multi-step reasoning and complex web navigation. By leveraging our curated high-quality dataset, we successfully develop advanced web agent WebExplorer-8B through supervised fine-tuning followed by reinforcement learning. Our model supports 128K context length and up to 100 tool calling turns, enabling long-horizon problem solving. Across diverse information-seeking benchmarks, WebExplorer-8B achieves the state-of-the-art performance at its scale. Notably, as an 8B-sized model, WebExplorer-8B is able to effectively search over an average of 16 turns after RL training, achieving higher accuracy than WebSailor-72B on BrowseComp-en/zh and attaining the best performance among models up to 100B parameters on WebWalkerQA and FRAMES. Beyond these information-seeking tasks, our model also achieves strong generalization on the HLE benchmark even though it is only trained on knowledge-intensive QA data. These results highlight our approach as a practical path toward long-horizon web agents.

