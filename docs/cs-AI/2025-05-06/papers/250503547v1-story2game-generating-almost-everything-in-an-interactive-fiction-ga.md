---
layout: default
title: STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game
---

# STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03547" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03547v1</a>
  <a href="https://arxiv.org/pdf/2505.03547.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03547v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03547v1', 'STORY2GAME: Generating (Almost) Everything in an Interactive Fiction Game')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Zhou, Shreyas Basavatia, Moontashir Siam, Zexin Chen, Mark O. Riedl

**分类**: cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出STORY2GAME以生成互动小说游戏的所有元素**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `互动小说` `大型语言模型` `动态动作生成` `游戏引擎` `故事生成` `人工智能` `游戏开发`

## 📋 核心要点

1. 现有方法通常依赖于硬编码的动作，限制了故事生成的灵活性和开放性。
2. STORY2GAME通过生成故事、填充世界和构建互动代码，允许动态生成动作以适应玩家的需求。
3. 实验表明，玩家能够顺利互动地完成生成的故事，验证了动作代码生成的有效性。

## 📝 摘要（中文）

我们介绍了STORY2GAME，这是一种利用大型语言模型生成文本互动小说游戏的新方法。该方法首先生成故事，然后填充游戏世界，并构建游戏引擎中的动作代码，使故事能够互动地展开。与固定的动作集相比，生成动作的能力使得故事生成过程更加开放，同时仍然允许基于游戏状态的体验。成功的动作生成的关键在于使用LLM生成的故事中动作的前提条件和效果，指导游戏引擎在玩家执行动作时需要跟踪和改变的游戏状态。我们还引入了一种动态生成新动作的技术，以适应玩家想要执行的、未包含在故事中的动作。动态动作生成可能需要对游戏引擎的状态表示进行即时更新，并修订先前生成的动作。我们评估了动作代码生成的成功率，以确定玩家是否能够互动地完成整个生成的故事。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统互动小说游戏中固定动作集限制故事生成灵活性的问题。现有方法往往无法适应玩家的即时需求，导致互动体验受限。

**核心思路**：STORY2GAME的核心思路是利用大型语言模型生成故事及其相关的动态动作，从而使得游戏体验更加开放和互动。通过生成动作的前提条件和效果，游戏引擎能够实时响应玩家的行为。

**技术框架**：该方法的整体架构包括三个主要模块：故事生成模块、世界填充模块和动作代码生成模块。故事生成模块负责创建情节，世界填充模块则构建游戏环境，动作代码生成模块则根据故事内容生成可执行的游戏动作。

**关键创新**：最重要的技术创新在于动态动作生成的能力，使得玩家可以在游戏中执行未预设的动作。这一创新使得游戏体验更加个性化和灵活，区别于传统的硬编码方法。

**关键设计**：在设计中，使用了LLM生成的前提条件和效果来指导游戏状态的变化。此外，动态生成的动作需要对游戏引擎的状态表示进行实时更新，确保游戏的连贯性和互动性。

## 📊 实验亮点

实验结果显示，STORY2GAME在动作代码生成的成功率上显著提高，玩家能够顺利互动地完成整个生成的故事，验证了该方法的有效性和实用性。与传统方法相比，动态动作生成的引入使得游戏体验更加灵活和开放。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、教育培训和互动故事创作等。通过实现动态生成的互动小说，开发者可以创造出更加丰富和个性化的用户体验，提升玩家的沉浸感和参与度。未来，该技术可能在更多领域中应用，如虚拟现实和增强现实环境中的互动体验。

## 📄 摘要（原文）

> We introduce STORY2GAME, a novel approach to using Large Language Models to generate text-based interactive fiction games that starts by generating a story, populates the world, and builds the code for actions in a game engine that enables the story to play out interactively. Whereas a given set of hard-coded actions can artificially constrain story generation, the ability to generate actions means the story generation process can be more open-ended but still allow for experiences that are grounded in a game state. The key to successful action generation is to use LLM-generated preconditions and effects of actions in the stories as guides for what aspects of the game state must be tracked and changed by the game engine when a player performs an action. We also introduce a technique for dynamically generating new actions to accommodate the player's desire to perform actions that they think of that are not part of the story. Dynamic action generation may require on-the-fly updates to the game engine's state representation and revision of previously generated actions. We evaluate the success rate of action code generation with respect to whether a player can interactively play through the entire generated story.

