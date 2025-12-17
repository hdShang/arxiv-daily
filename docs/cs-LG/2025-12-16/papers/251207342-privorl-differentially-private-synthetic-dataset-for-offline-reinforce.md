---
layout: default
title: PrivORL: Differentially Private Synthetic Dataset for Offline Reinforcement Learning
---

# PrivORL: Differentially Private Synthetic Dataset for Offline Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.07342" class="toolbar-btn" target="_blank">📄 arXiv: 2512.07342</a>
  <a href="https://arxiv.org/pdf/2512.07342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.07342" onclick="toggleFavorite(this, '2512.07342', 'PrivORL: Differentially Private Synthetic Dataset for Offline Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Gong, Zheng Liu, Kecen Li, Tianhao Wang

**分类**: cs.CR, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**PrivORL：一种差分隐私离线强化学习合成数据集生成方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `差分隐私` `数据集合成` `扩散模型` `扩散Transformer` `隐私保护` `数据效用`

## 📋 核心要点

1. 离线强化学习数据集存在隐私泄露风险，需要保护数据集中包含的敏感信息。
2. PrivORL利用扩散模型和扩散Transformer，在差分隐私保护下合成高质量的转移和轨迹数据。
3. 实验表明，PrivORL在效用性和保真度方面优于现有方法，能够生成更逼真的合成数据集。

## 📝 摘要（中文）

离线强化学习(RL)已成为一种流行的RL范式。在离线RL中，数据提供者共享预先收集的数据集（单个转移或形成轨迹的转移序列），以支持RL模型（也称为智能体）的训练，而无需与环境直接交互。离线RL节省了与环境的交互，并且在导航等关键领域非常有效。与此同时，离线RL数据集中的隐私泄露问题日益突出。为了保护离线RL数据集中的隐私信息，我们提出了第一个差分隐私(DP)离线数据集合成方法PrivORL，它利用扩散模型和扩散Transformer分别在DP下合成转移和轨迹。然后，可以安全地发布合成数据集，用于下游分析和研究。PrivORL采用了一种流行的方法，即在公共数据集上预训练合成器，然后使用DP随机梯度下降(DP-SGD)在敏感数据集上进行微调。此外，PrivORL引入了好奇心驱动的预训练，它利用来自好奇心模块的反馈来多样化合成数据集，从而可以生成与敏感数据集非常相似的各种合成转移和轨迹。在五个敏感离线RL数据集上的大量实验表明，与基线方法相比，我们的方法在DP转移和轨迹合成中都实现了更好的效用和保真度。

## 🔬 方法详解

**问题定义**：论文旨在解决离线强化学习中数据集的隐私泄露问题。现有的离线强化学习方法依赖于预先收集的数据集，这些数据集可能包含敏感信息。直接使用这些数据集进行模型训练会带来隐私泄露的风险，因此需要一种方法来生成既能保护隐私又能保留数据集特征的合成数据集。

**核心思路**：论文的核心思路是利用差分隐私(DP)技术，结合扩散模型和扩散Transformer，生成既能保护隐私又能保留原始数据集特征的合成数据集。通过在公共数据集上预训练合成器，然后在敏感数据集上进行差分隐私微调，可以有效地平衡隐私保护和数据效用。

**技术框架**：PrivORL的整体框架包括以下几个主要阶段：1) 在公共数据集上预训练扩散模型和扩散Transformer；2) 在敏感数据集上使用DP-SGD对预训练模型进行微调；3) 使用微调后的模型生成合成的转移和轨迹数据。其中，扩散模型用于生成单个转移，扩散Transformer用于生成轨迹。

**关键创新**：PrivORL的关键创新在于以下几个方面：1) 首次将扩散模型和扩散Transformer应用于差分隐私离线强化学习数据集合成；2) 提出了好奇心驱动的预训练方法，利用好奇心模块的反馈来多样化合成数据集，提高数据质量；3) 实现了在差分隐私保护下生成高质量的转移和轨迹数据，有效平衡了隐私保护和数据效用。

**关键设计**：PrivORL的关键设计包括：1) 使用DP-SGD进行微调，以保证差分隐私；2) 设计好奇心模块，鼓励模型探索更多样化的状态空间；3) 使用扩散模型和扩散Transformer分别生成转移和轨迹，充分利用了两种模型的优势；4) 损失函数的设计，旨在最小化合成数据与原始数据之间的差异，同时满足差分隐私约束。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.07342/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.07342/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.07342/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PrivORL在五个敏感离线RL数据集上取得了显著的性能提升。与基线方法相比，PrivORL在DP转移和轨迹合成中都实现了更好的效用和保真度。具体来说，PrivORL能够生成更逼真的合成数据集，使得在合成数据集上训练的RL智能体能够获得与在原始数据集上训练的智能体相近的性能。

## 🎯 应用场景

PrivORL可应用于各种需要保护隐私的离线强化学习场景，例如医疗、金融和自动驾驶等领域。通过生成差分隐私的合成数据集，可以安全地共享数据，促进算法研究和模型训练，同时避免敏感信息的泄露。该方法有助于推动离线强化学习在隐私敏感领域的应用。

## 📄 摘要（原文）

> Recently, offline reinforcement learning (RL) has become a popular RL paradigm. In offline RL, data providers share pre-collected datasets -- either as individual transitions or sequences of transitions forming trajectories -- to enable the training of RL models (also called agents) without direct interaction with the environments. Offline RL saves interactions with environments compared to traditional RL, and has been effective in critical areas, such as navigation tasks. Meanwhile, concerns about privacy leakage from offline RL datasets have emerged.To safeguard private information in offline RL datasets, we propose the first differential privacy (DP) offline dataset synthesis method, PrivORL, which leverages a diffusion model and diffusion transformer to synthesize transitions and trajectories, respectively, under DP. The synthetic dataset can then be securely released for downstream analysis and research. PrivORL adopts the popular approach of pre-training a synthesizer on public datasets, and then fine-tuning on sensitive datasets using DP Stochastic Gradient Descent (DP-SGD). Additionally, PrivORL introduces curiosity-driven pre-training, which uses feedback from the curiosity module to diversify the synthetic dataset and thus can generate diverse synthetic transitions and trajectories that closely resemble the sensitive dataset. Extensive experiments on five sensitive offline RL datasets show that our method achieves better utility and fidelity in both DP transition and trajectory synthesis compared to baselines. The replication package is available at the GitHub repository.

