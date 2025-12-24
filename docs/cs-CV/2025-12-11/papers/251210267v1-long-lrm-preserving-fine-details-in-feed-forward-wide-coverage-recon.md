---
layout: default
title: "Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction"
---

# Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10267" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10267v1</a>
  <a href="https://arxiv.org/pdf/2512.10267.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10267v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10267v1', 'Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Ziwen, Hao Tan, Peng Wang, Zexiang Xu, Li Fuxin

**分类**: cs.CV

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**Long-LRM++：结合半显式表达与轻量解码器，实现高质量、实时的宽覆盖场景重建。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `三维重建` `高斯溅射` `隐式表达` `实时渲染` `半显式表示` `轻量级解码器` `多视角重建` `场景重建`

## 📋 核心要点

1. 现有通用高斯溅射方法在重建精细结构时易出现模糊，隐式表达方法渲染质量高但计算量大，难以实时渲染。
2. Long-LRM++采用半显式场景表示，结合轻量级解码器，旨在兼顾渲染质量和实时性，实现高效的场景重建。
3. 实验表明，Long-LRM++在DL3DV数据集上达到LaCT的渲染质量，并在A100 GPU上实现14 FPS的实时渲染，同时具备良好的泛化能力。

## 📝 摘要（中文）

通用高斯溅射(GS)的最新进展使得能够从数十个输入视图进行前馈场景重建。Long-LRM显著地将这种范式扩展到32个输入图像，分辨率为950x540，从而在单个前向传递中实现360°场景级重建。然而，直接一次性预测数百万个高斯参数仍然对误差高度敏感：位置或其他属性上的微小不准确会导致明显的模糊，尤其是在文本等精细结构中。与此同时，LVSM和LaCT等隐式表示方法通过将场景信息压缩到模型权重中，而不是显式高斯中，并使用完整的transformer或TTT骨干解码RGB帧，从而展示了显著更高的渲染保真度。然而，对于每个渲染帧的这种计算密集型解压缩过程使得实时渲染变得不可行。这些观察结果提出了关键问题：深度、顺序的“解压缩”过程是必要的吗？我们能否在保持隐式表示优势的同时实现实时性能？我们使用Long-LRM++来解决这些问题，Long-LRM++采用半显式场景表示，并结合轻量级解码器。Long-LRM++在DL3DV上匹配了LaCT的渲染质量，同时在A100 GPU上实现了实时14 FPS渲染，克服了先前隐式方法的速度限制。我们的设计还扩展到64个输入视图，分辨率为950x540，展示了对增加的输入长度的强大泛化能力。此外，与直接从高斯渲染深度相比，Long-LRM++在ScanNetv2上提供了卓越的新视角深度预测。广泛的消融研究验证了所提出框架中每个组件的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决从多视角图像重建三维场景的问题，尤其关注如何在保证渲染质量（特别是精细结构）的同时，实现实时渲染。现有方法，如Long-LRM，虽然能快速重建，但在精细结构上存在模糊；而隐式表达方法，如LaCT，虽然渲染质量高，但计算量大，无法实时渲染。

**核心思路**：论文的核心思路是采用一种半显式的场景表示方法，即不完全依赖显式的高斯参数，也不完全依赖隐式的模型权重。通过结合显式表达的快速性和隐式表达的高质量，并设计一个轻量级的解码器，从而在渲染质量和速度之间取得平衡。

**技术框架**：Long-LRM++的整体架构包含以下几个主要模块：1) 多视角图像输入；2) 特征提取网络（可能是修改过的Long-LRM的encoder）；3) 半显式场景表示（例如，稀疏的高斯参数加上一些隐式特征）；4) 轻量级解码器，用于将半显式表示解码为RGB图像；5) 渲染模块，将解码后的信息渲染成最终图像。整个流程是一个前向过程，可以实现快速渲染。

**关键创新**：Long-LRM++的关键创新在于其半显式的场景表示和轻量级解码器的设计。与完全显式的方法相比，半显式表示能够更好地捕捉场景的细节信息；与完全隐式的方法相比，轻量级解码器能够显著降低计算复杂度，从而实现实时渲染。这种混合策略是该方法的核心创新。

**关键设计**：论文中可能包含以下关键设计细节：1) 半显式表示的具体形式，例如，高斯参数的数量、隐式特征的维度等；2) 轻量级解码器的网络结构，例如，卷积层、全连接层、注意力机制等；3) 损失函数的设计，例如，RGB重建损失、深度损失、正则化项等；4) 训练策略，例如，学习率、batch size、优化器等。这些细节对最终的性能至关重要，但具体细节需要参考论文原文。

## 📊 实验亮点

Long-LRM++在DL3DV数据集上达到了与LaCT相当的渲染质量，同时在A100 GPU上实现了14 FPS的实时渲染，显著优于现有隐式表达方法的速度。此外，Long-LRM++在ScanNetv2数据集上实现了更好的新视角深度预测，并且能够扩展到64个输入视图，展示了良好的泛化能力。消融实验验证了各个组件的有效性。

## 🎯 应用场景

Long-LRM++在三维重建领域具有广泛的应用前景，例如虚拟现实、增强现实、机器人导航、自动驾驶、游戏开发等。该方法能够快速、高质量地重建场景，为用户提供沉浸式的体验，并为机器人提供准确的环境感知信息。未来，该方法有望应用于更大规模、更复杂的场景重建，并与其他技术相结合，实现更智能化的应用。

## 📄 摘要（原文）

> Recent advances in generalizable Gaussian splatting (GS) have enabled feed-forward reconstruction of scenes from tens of input views. Long-LRM notably scales this paradigm to 32 input images at $950\times540$ resolution, achieving 360° scene-level reconstruction in a single forward pass. However, directly predicting millions of Gaussian parameters at once remains highly error-sensitive: small inaccuracies in positions or other attributes lead to noticeable blurring, particularly in fine structures such as text. In parallel, implicit representation methods such as LVSM and LaCT have demonstrated significantly higher rendering fidelity by compressing scene information into model weights rather than explicit Gaussians, and decoding RGB frames using the full transformer or TTT backbone. However, this computationally intensive decompression process for every rendered frame makes real-time rendering infeasible. These observations raise key questions: Is the deep, sequential "decompression" process necessary? Can we retain the benefits of implicit representations while enabling real-time performance? We address these questions with Long-LRM++, a model that adopts a semi-explicit scene representation combined with a lightweight decoder. Long-LRM++ matches the rendering quality of LaCT on DL3DV while achieving real-time 14 FPS rendering on an A100 GPU, overcoming the speed limitations of prior implicit methods. Our design also scales to 64 input views at the $950\times540$ resolution, demonstrating strong generalization to increased input lengths. Additionally, Long-LRM++ delivers superior novel-view depth prediction on ScanNetv2 compared to direct depth rendering from Gaussians. Extensive ablation studies validate the effectiveness of each component in the proposed framework.

