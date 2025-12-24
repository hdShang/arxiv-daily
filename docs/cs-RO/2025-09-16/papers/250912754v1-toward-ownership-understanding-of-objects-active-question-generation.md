---
layout: default
title: "Toward Ownership Understanding of Objects: Active Question Generation with Large Language Model and Probabilistic Generative Model"
---

# Toward Ownership Understanding of Objects: Active Question Generation with Large Language Model and Probabilistic Generative Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12754" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12754v1</a>
  <a href="https://arxiv.org/pdf/2509.12754.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12754v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12754v1', 'Toward Ownership Understanding of Objects: Active Question Generation with Large Language Model and Probabilistic Generative Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saki Hashimoto, Shoichi Hasegawa, Tomochika Ishikawa, Akira Taniguchi, Yoshinobu Hagiwara, Lotfi El Hafi, Tadahiro Taniguchi

**分类**: cs.RO, cs.AI, cs.HC, cs.LG

**发布日期**: 2025-09-16

**备注**: Submitted to AROB-ISBC 2026 (Journal Track option)

---

## 💡 一句话要点

**ActOwL：结合LLM与概率生成模型的主动问答，提升机器人对象所有权理解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人` `所有权理解` `主动学习` `大型语言模型` `概率生成模型`

## 📋 核心要点

1. 机器人需要在家庭和办公环境中理解物体所有权，但仅凭视觉特征难以可靠推断。
2. ActOwL框架结合概率生成模型和大型语言模型，主动提问并学习物体所有权。
3. 实验表明，ActOwL能以更少的问题显著提高所有权聚类准确率。

## 📝 摘要（中文）

本文提出了一种名为主动所有权学习（ActOwL）的框架，旨在使机器人能够主动生成并向用户提问有关对象所有权的问题。该框架利用概率生成模型选择能够最大化信息增益的问题，从而高效地获取所有权知识，提高学习效率。此外，ActOwL还利用大型语言模型（LLM）中的常识知识，预先将对象分类为共享或自有，并仅针对自有对象进行提问。在模拟家庭环境和真实实验室环境中的实验表明，与基线方法相比，ActOwL以更少的问题实现了显着更高的所有权聚类准确率。这些发现证明了将主动推理与LLM引导的常识推理相结合的有效性，从而提高了机器人获取所有权知识的能力，以实现实际且符合社会规范的任务执行。

## 🔬 方法详解

**问题定义**：机器人需要在复杂环境中理解物体的所有权关系，以便正确执行“把我的杯子拿来”之类的指令。然而，仅仅依靠视觉信息来判断物体的所有权是不可靠的，因为外观相似的物体可能属于不同的人。现有的方法通常依赖于被动地观察和学习，效率低下，且难以处理复杂的所有权关系。

**核心思路**：ActOwL的核心思路是让机器人主动地向用户提问，通过交互式学习来获取物体的所有权信息。通过主动提问，机器人可以更有针对性地获取信息，提高学习效率。此外，该方法还利用大型语言模型（LLM）的常识知识来辅助判断，减少不必要的提问。

**技术框架**：ActOwL框架主要包含以下几个模块：1) 对象检测模块：用于识别场景中的物体；2) LLM预分类模块：利用LLM的常识知识将物体预分类为共享或自有；3) 概率生成模型：用于生成候选问题，并评估每个问题的信息增益；4) 问题选择模块：选择信息增益最大的问题向用户提问；5) 所有权学习模块：根据用户的回答更新所有权知识。整个流程是，首先检测场景中的物体，然后利用LLM进行预分类，接着通过概率生成模型生成问题并选择最优问题提问，最后根据用户回答更新所有权知识。

**关键创新**：ActOwL的关键创新在于将主动问答与LLM的常识知识相结合。传统的机器人所有权学习方法通常是被动的，效率较低。ActOwL通过主动提问，可以更有针对性地获取信息。同时，利用LLM的常识知识可以减少不必要的提问，提高学习效率。这种结合使得机器人能够更有效地学习物体的所有权关系。

**关键设计**：概率生成模型的设计是关键。该模型需要能够生成多样化的、信息量大的问题。论文中具体采用了哪种概率生成模型（例如贝叶斯网络、隐马尔可夫模型等）以及如何设计模型的参数，摘要中没有明确说明，属于未知信息。此外，如何利用LLM的输出来指导问题生成和选择，以及如何将用户的回答融入到所有权学习模型中，也是关键的设计细节，但摘要中没有详细描述。

## 📊 实验亮点

实验结果表明，ActOwL在模拟家庭环境和真实实验室环境中均取得了显著的性能提升。与基线方法相比，ActOwL能够以更少的问题达到更高的所有权聚类准确率。具体的数据提升幅度在摘要中没有给出，属于未知信息。这证明了ActOwL框架的有效性，以及将主动推理与LLM引导的常识推理相结合的优势。

## 🎯 应用场景

该研究成果可应用于家庭服务机器人、办公助手机器人等领域，帮助机器人更好地理解人类指令，提供更个性化的服务。例如，机器人可以根据用户的所有权信息，准确地找到用户需要的物品，避免拿错东西。未来，该技术还可以扩展到更复杂的场景，例如多人协作环境，帮助机器人理解不同用户之间的所有权关系。

## 📄 摘要（原文）

> Robots operating in domestic and office environments must understand object ownership to correctly execute instructions such as ``Bring me my cup.'' However, ownership cannot be reliably inferred from visual features alone. To address this gap, we propose Active Ownership Learning (ActOwL), a framework that enables robots to actively generate and ask ownership-related questions to users. ActOwL employs a probabilistic generative model to select questions that maximize information gain, thereby acquiring ownership knowledge efficiently to improve learning efficiency. Additionally, by leveraging commonsense knowledge from Large Language Models (LLM), objects are pre-classified as either shared or owned, and only owned objects are targeted for questioning. Through experiments in a simulated home environment and a real-world laboratory setting, ActOwL achieved significantly higher ownership clustering accuracy with fewer questions than baseline methods. These findings demonstrate the effectiveness of combining active inference with LLM-guided commonsense reasoning, advancing the capability of robots to acquire ownership knowledge for practical and socially appropriate task execution.

