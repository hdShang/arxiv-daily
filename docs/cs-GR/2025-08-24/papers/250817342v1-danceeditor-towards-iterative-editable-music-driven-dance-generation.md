---
layout: default
title: "DanceEditor: Towards Iterative Editable Music-driven Dance Generation with Open-Vocabulary Descriptions"
---

# DanceEditor: Towards Iterative Editable Music-driven Dance Generation with Open-Vocabulary Descriptions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17342" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17342v1</a>
  <a href="https://arxiv.org/pdf/2508.17342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17342v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17342v1', 'DanceEditor: Towards Iterative Editable Music-driven Dance Generation with Open-Vocabulary Descriptions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengyuan Zhang, Zhe Li, Xingqun Qi, Mengze Li, Muyi Sun, Man Zhang, Sirui Han

**分类**: cs.GR, cs.CV, cs.MM, cs.SD

**发布日期**: 2025-08-24

**期刊**: ICCV 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://lzvsdy.github.io/DanceEditor/)

---

## 💡 一句话要点

**提出DanceEditor以解决舞蹈生成与编辑的实际需求**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `舞蹈生成` `可编辑舞蹈` `多模态融合` `音乐驱动` `虚拟角色动画`

## 📋 核心要点

1. 现有方法在舞蹈生成中未考虑用户对舞蹈动作的编辑需求，且缺乏支持迭代编辑的高质量数据集。
2. 论文提出DanceEditor框架，通过预测-再编辑的方式，结合音乐和文本描述，实现可编辑的舞蹈生成。
3. 实验结果显示，DanceEditor在DanceRemix数据集上显著优于现有模型，展示了更高的生成质量和编辑灵活性。

## 📝 摘要（中文）

从音乐信号生成连贯且多样的人类舞蹈在虚拟角色动画中取得了显著进展。然而，现有方法仅支持直接舞蹈合成，未考虑到用户在实际编舞场景中对舞蹈动作进行编辑的需求。此外，缺乏高质量的舞蹈数据集以支持迭代编辑也限制了这一挑战的解决。为此，我们构建了DanceRemix，一个包含超过2530万舞蹈帧和8.45万对的多轮可编辑舞蹈数据集，并提出了名为DanceEditor的新框架，旨在与给定音乐信号一致地进行迭代和可编辑的舞蹈生成。该框架采用预测-再编辑的范式，结合多模态条件，提升了生成结果的权威性，并通过交叉模态编辑模块（CEM）实现了与音乐和文本提示的动态整合。实验表明，我们的方法在新收集的DanceRemix数据集上优于现有的最先进模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有舞蹈生成方法无法满足用户对舞蹈动作编辑需求的问题。现有方法主要集中于直接生成舞蹈，缺乏对迭代编辑的支持，且缺少高质量的舞蹈数据集以进行有效训练。

**核心思路**：论文提出的DanceEditor框架采用预测-再编辑的范式，首先根据音乐信号生成初步舞蹈动作，然后通过用户提供的文本描述进行迭代编辑。这种设计使得生成的舞蹈既能与音乐节奏相协调，又能灵活响应用户的编辑需求。

**技术框架**：DanceEditor的整体架构包括两个主要阶段：初步预测阶段和迭代编辑阶段。在初步预测阶段，框架直接从对齐的音乐信号中建模舞蹈动作；在迭代编辑阶段，通过交叉模态编辑模块（CEM）将初步生成的舞蹈与音乐和文本提示结合，生成可编辑的舞蹈序列。

**关键创新**：最重要的技术创新在于引入了交叉模态编辑模块（CEM），该模块能够动态整合初步生成的舞蹈、音乐和文本提示，确保生成结果在音乐和语义上都保持一致。这一创新使得DanceEditor在舞蹈生成和编辑的灵活性上优于现有方法。

**关键设计**：在技术细节方面，CEM模块通过时间运动线索自适应地引导合成序列，确保生成的舞蹈不仅符合音乐的和声特征，还能与文本描述保持细粒度的语义对齐。

## 📊 实验亮点

在实验中，DanceEditor在新收集的DanceRemix数据集上表现出色，生成质量显著优于现有最先进模型，具体性能提升幅度达到XX%（具体数据未知），展示了其在舞蹈生成与编辑任务中的有效性和灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和舞蹈教育等。通过实现音乐驱动的可编辑舞蹈生成，DanceEditor能够为用户提供更直观的舞蹈创作工具，促进舞蹈艺术的传播与发展，未来可能在娱乐和教育行业产生深远影响。

## 📄 摘要（原文）

> Generating coherent and diverse human dances from music signals has gained tremendous progress in animating virtual avatars. While existing methods support direct dance synthesis, they fail to recognize that enabling users to edit dance movements is far more practical in real-world choreography scenarios. Moreover, the lack of high-quality dance datasets incorporating iterative editing also limits addressing this challenge. To achieve this goal, we first construct DanceRemix, a large-scale multi-turn editable dance dataset comprising the prompt featuring over 25.3M dance frames and 84.5K pairs. In addition, we propose a novel framework for iterative and editable dance generation coherently aligned with given music signals, namely DanceEditor. Considering the dance motion should be both musical rhythmic and enable iterative editing by user descriptions, our framework is built upon a prediction-then-editing paradigm unifying multi-modal conditions. At the initial prediction stage, our framework improves the authority of generated results by directly modeling dance movements from tailored, aligned music. Moreover, at the subsequent iterative editing stages, we incorporate text descriptions as conditioning information to draw the editable results through a specifically designed Cross-modality Editing Module (CEM). Specifically, CEM adaptively integrates the initial prediction with music and text prompts as temporal motion cues to guide the synthesized sequences. Thereby, the results display music harmonics while preserving fine-grained semantic alignment with text descriptions. Extensive experiments demonstrate that our method outperforms the state-of-the-art models on our newly collected DanceRemix dataset. Code is available at https://lzvsdy.github.io/DanceEditor/.

