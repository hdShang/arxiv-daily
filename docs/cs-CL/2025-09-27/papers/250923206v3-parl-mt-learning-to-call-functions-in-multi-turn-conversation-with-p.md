---
layout: default
title: "PARL-MT: Learning to Call Functions in Multi-Turn Conversation with Progress Awareness"
---

# PARL-MT: Learning to Call Functions in Multi-Turn Conversation with Progress Awareness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23206" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23206v3</a>
  <a href="https://arxiv.org/pdf/2509.23206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23206v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23206v3', 'PARL-MT: Learning to Call Functions in Multi-Turn Conversation with Progress Awareness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huacan Chai, Zijie Cao, Maolin Ran, Yingxuan Yang, Jianghao Lin, Xin Peng, Hairui Wang, Renjie Ding, Ziyu Wan, Muning Wen, Weiwen Liu, Weinan Zhang, Fei Huang, Ying Wen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27 (更新: 2025-10-09)

---

## 💡 一句话要点

**PARL-MT：通过进度感知学习在多轮对话中调用函数**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `函数调用` `大型语言模型` `进度感知` `强化学习`

## 📋 核心要点

1. 现有方法在多轮对话函数调用中缺乏任务级规划，或使用端到端强化学习存在冗余和缺乏进度感知。
2. PARL-MT框架通过进度感知生成(PAG)和进度感知引导的强化学习(PAG-RL)将进度感知融入LLM训练。
3. 实验结果表明，PARL-MT在两个公共基准上显著优于现有方法，验证了进度感知的有效性。

## 📝 摘要（中文）

大型语言模型(LLMs)在单轮函数调用中取得了显著成功，但旅行规划或多阶段数据分析等实际应用通常发生在多轮对话中。在这些场景中，LLMs不仅必须在每个步骤中发出准确的函数调用，还必须保持进度感知，即总结过去交互并规划未来行动以确保连贯的、长期的任务执行能力。然而，现有方法要么将多轮训练简化为孤立的单轮样本，忽略了任务级别的规划，要么采用端到端强化学习(RL)，这种方法存在冗余问题，并且缺乏对进度感知的显式集成。为了克服这些限制，我们引入了PARL-MT，这是一个将进度感知显式地融入到LLM多轮函数调用训练中的框架。PARL-MT结合了(i)一个进度感知生成(PAG)管道，该管道自动构建将对话摘要与未来任务规划相结合的数据集，以及(ii)一个进度感知引导的强化学习(PAG-RL)算法，该算法将进度感知集成到RL训练中，以减少上下文冗余并提高局部动作与全局任务完成之间的一致性。在两个公共基准上的实验结果表明，PARL-MT显著优于现有方法，突出了进度感知在实现鲁棒和高效的多轮函数调用方面的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在多轮对话场景下进行函数调用时，缺乏对对话历史的总结和未来任务规划能力的问题。现有方法要么将多轮对话简化为单轮对话，忽略了任务级别的规划；要么采用端到端强化学习，但这种方法容易产生冗余，并且没有显式地整合进度感知。

**核心思路**：论文的核心思路是通过显式地将进度感知融入到LLM的训练过程中，使其能够更好地理解对话历史，并根据当前状态规划未来的动作。具体来说，论文提出了一个包含进度感知生成(PAG)和进度感知引导的强化学习(PAG-RL)的框架，从而提升LLM在多轮对话中函数调用的准确性和效率。

**技术框架**：PARL-MT框架主要包含两个阶段：(1) 进度感知生成(PAG)：该阶段自动构建数据集，将对话摘要与未来任务规划相结合，为后续的强化学习提供训练数据。(2) 进度感知引导的强化学习(PAG-RL)：该阶段将进度感知集成到强化学习训练中，以减少上下文冗余，并提高局部动作与全局任务完成之间的一致性。PAG-RL利用PAG生成的数据来指导强化学习过程，从而使LLM能够更好地学习如何在多轮对话中进行函数调用。

**关键创新**：论文的关键创新在于显式地将进度感知融入到LLM的多轮对话函数调用训练中。与现有方法相比，PARL-MT能够更好地理解对话历史，并根据当前状态规划未来的动作，从而提高了函数调用的准确性和效率。PAG和PAG-RL的结合是实现这一目标的关键。

**关键设计**：PAG管道的具体实现细节未知，但其核心目标是生成包含对话摘要和未来任务规划的数据集。PAG-RL算法的关键在于如何将进度感知信息有效地融入到强化学习的奖励函数和状态表示中。具体的奖励函数设计和状态表示方式未知，但需要能够反映对话的进度和未来的任务目标。此外，强化学习算法的选择和超参数的调整也是影响性能的关键因素。

## 📊 实验亮点

PARL-MT在两个公共基准测试中显著优于现有方法，证明了进度感知在多轮函数调用中的有效性。具体的性能提升数据未知，但摘要中明确指出PARL-MT取得了显著的性能提升。实验结果表明，通过显式地将进度感知融入到LLM的训练过程中，可以有效地提高其在多轮对话中函数调用的准确性和效率。

## 🎯 应用场景

该研究成果可应用于各种需要多轮对话和函数调用的场景，例如智能助手、旅行规划、数据分析等。通过提高LLM在多轮对话中函数调用的准确性和效率，可以显著提升用户体验，并降低人工干预的需求。未来，该技术有望在更广泛的领域得到应用，例如智能客服、自动化流程等。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved impressive success in single-turn function calling, yet real-world applications such as travel planning or multi-stage data analysis typically unfold across multi-turn conversations. In these settings, LLMs must not only issue accurate function calls at each step but also maintain progress awareness, the ability to summarize past interactions and plan future actions to ensure coherent, long-horizon task execution. Existing approaches, however, either reduce multi-turn training to isolated single-turn samples, which neglects task-level planning, or employ end-to-end reinforcement learning (RL) that struggles with redundancy and lacks explicit integration of progress awareness. To overcome these limitations, we introduce PARL-MT, a framework that explicitly incorporates progress awareness into LLM training for multi-turn function calling. PARL-MT combines (i) a Progress Awareness Generation (PAG) pipeline, which automatically constructs datasets coupling conversation summaries with future task planning, and (ii) a Progress Awareness-Guided Reinforcement Learning (PAG-RL) algorithm, which integrates progress awareness into RL training to reduce contextual redundancy and improve alignment between local actions and global task completion. Empirical results on two public benchmarks demonstrate that PARL-MT significantly outperforms existing methods, highlighting the effectiveness of progress awareness in enabling robust and efficient multi-turn function calling.

