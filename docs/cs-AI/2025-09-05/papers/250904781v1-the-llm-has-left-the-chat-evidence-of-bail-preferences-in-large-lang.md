---
layout: default
title: "The LLM Has Left The Chat: Evidence of Bail Preferences in Large Language Models"
---

# The LLM Has Left The Chat: Evidence of Bail Preferences in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04781" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04781v1</a>
  <a href="https://arxiv.org/pdf/2509.04781.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04781v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04781v1', 'The LLM Has Left The Chat: Evidence of Bail Preferences in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Danielle Ensign, Henry Sleight, Kyle Fish

**分类**: cs.CY, cs.AI, cs.LG

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**研究大型语言模型中的“退出对话”偏好，揭示模型在不同情境下的退出行为。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `退出行为` `对话系统` `安全性` `BailBench` `拒绝率` `越狱攻击`

## 📋 核心要点

1. 大型语言模型在对话中可能存在不期望的“退出”行为，影响用户体验和系统可靠性。
2. 通过设计多种退出机制（工具、字符串、提示），系统性地评估LLM在不同情境下的退出倾向。
3. 构建了BailBench数据集，用于评估和比较不同LLM的退出行为，并分析了退出与拒绝之间的关系。

## 📝 摘要（中文）

本文研究了大型语言模型（LLM）在给定选择时是否会选择退出对话（bail）。研究通过三种不同的退出方法来评估模型：模型可以调用的退出工具、模型可以输出的退出字符串以及询问模型是否想离开的退出提示。在真实世界数据的延续（Wildchat和ShareGPT）上，所有这三种退出方法都发现模型大约在0.28-32%的时间内会退出（取决于模型和退出方法）。然而，研究发现退出率可能严重依赖于用于转录的模型，这意味着我们可能高估了高达4倍的真实世界退出率。如果考虑到退出提示的误报（22%），我们估计真实世界退出率范围为0.06-7%，具体取决于模型和退出方法。我们使用从真实世界数据延续中的观察结果来构建退出案例的非详尽分类法，并使用此分类法来构建BailBench：一个代表性的合成数据集，其中包含一些模型退出的情况。我们在该数据集上测试了许多模型，并观察到大多数模型都出现了一些退出行为。不同模型、退出方法和提示措辞之间的退出率差异很大。最后，我们研究了拒绝和退出之间的关系。我们发现：1）真实世界对话延续的0-13%导致了退出，但没有相应的拒绝；2）越狱往往会降低拒绝率，但会增加退出率；3）拒绝消除会增加无拒绝退出率，但仅适用于某些退出方法；4）BailBench上的拒绝率似乎无法预测退出率。

## 🔬 方法详解

**问题定义**：本文旨在研究大型语言模型（LLM）在对话过程中，在何种情况下会选择退出（bail out）对话。现有方法缺乏对LLM退出行为的系统性评估和理解，难以预测和控制模型的退出行为，影响了对话系统的稳定性和用户体验。

**核心思路**：核心思路是通过多种方式赋予LLM退出对话的能力，并观察其在不同情境下的退出行为。通过分析退出行为的模式，构建退出案例的分类法，并基于此构建合成数据集BailBench，用于更全面地评估和比较不同LLM的退出倾向。

**技术框架**：研究主要包含以下几个阶段：1) 设计三种退出机制：退出工具（bail tool）、退出字符串（bail string）和退出提示（bail prompt）。2) 在真实世界对话数据（Wildchat和ShareGPT）上进行实验，观察LLM的退出行为。3) 分析退出案例，构建退出案例分类法。4) 基于分类法构建合成数据集BailBench。5) 在BailBench上评估多个LLM的退出行为，并分析退出与拒绝之间的关系。

**关键创新**：关键创新在于对LLM退出行为的系统性研究，包括：1) 提出了多种退出机制，用于评估LLM的退出倾向。2) 构建了BailBench数据集，用于更全面地评估和比较不同LLM的退出行为。3) 分析了退出与拒绝之间的关系，揭示了越狱攻击对退出行为的影响。

**关键设计**：研究中，退出工具的具体实现方式未知，退出字符串的设计也未详细说明。退出提示的设计可能影响模型的退出率，具体提示语的选择未知。BailBench数据集的构建基于人工分析的退出案例分类法，分类法的质量直接影响数据集的代表性。实验中使用的LLM的具体型号和参数设置未知。

## 📊 实验亮点

研究发现，LLM在真实世界对话延续中，退出率约为0.06-7%，但可能被高估。越狱攻击会降低拒绝率，但增加退出率。拒绝消除会增加无拒绝退出率，但仅适用于某些退出方法。BailBench上的拒绝率似乎无法预测退出率。

## 🎯 应用场景

该研究成果可应用于提升对话系统的稳定性和用户体验。通过理解和预测LLM的退出行为，可以设计更鲁棒的对话策略，避免模型在关键时刻退出对话。此外，BailBench数据集可用于评估和比较不同LLM的安全性，防止模型在不适当的场景下退出。

## 📄 摘要（原文）

> When given the option, will LLMs choose to leave the conversation (bail)? We investigate this question by giving models the option to bail out of interactions using three different bail methods: a bail tool the model can call, a bail string the model can output, and a bail prompt that asks the model if it wants to leave. On continuations of real world data (Wildchat and ShareGPT), all three of these bail methods find models will bail around 0.28-32\% of the time (depending on the model and bail method). However, we find that bail rates can depend heavily on the model used for the transcript, which means we may be overestimating real world bail rates by up to 4x. If we also take into account false positives on bail prompt (22\%), we estimate real world bail rates range from 0.06-7\%, depending on the model and bail method. We use observations from our continuations of real world data to construct a non-exhaustive taxonomy of bail cases, and use this taxonomy to construct BailBench: a representative synthetic dataset of situations where some models bail. We test many models on this dataset, and observe some bail behavior occurring for most of them. Bail rates vary substantially between models, bail methods, and prompt wordings. Finally, we study the relationship between refusals and bails. We find: 1) 0-13\% of continuations of real world conversations resulted in a bail without a corresponding refusal 2) Jailbreaks tend to decrease refusal rates, but increase bail rates 3) Refusal abliteration increases no-refuse bail rates, but only for some bail methods 4) Refusal rate on BailBench does not appear to predict bail rate.

