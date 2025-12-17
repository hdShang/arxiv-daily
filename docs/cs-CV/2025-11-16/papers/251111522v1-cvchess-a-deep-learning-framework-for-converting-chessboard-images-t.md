---
layout: default
title: CVChess: A Deep Learning Framework for Converting Chessboard Images to Forsyth-Edwards Notation
---

# CVChess: A Deep Learning Framework for Converting Chessboard Images to Forsyth-Edwards Notation

**arXiv**: [2511.11522v1](https://arxiv.org/abs/2511.11522) | [PDF](https://arxiv.org/pdf/2511.11522.pdf)

**作者**: Luthira Abeykoon, Ved Patel, Gawthaman Senthilvelan, Darshan Kasundra

---

## 💡 一句话要点

**提出CVChess框架，将棋盘图像转换为FEN以弥合物理与数字象棋体验差距**

**关键词**: `棋盘图像识别` `残差卷积神经网络` `FEN转换` `象棋引擎集成` `图像预处理`

## 📋 核心要点

1. 核心问题：物理象棋游戏缺乏数字辅助，导致与在线体验脱节
2. 方法要点：使用残差CNN进行棋子识别，结合图像预处理和分割步骤
3. 实验或效果：在ChessReD数据集上训练，输出FEN供引擎生成最优移动

## 📄 摘要（原文）

> Chess has experienced a large increase in viewership since the pandemic, driven largely by the accessibility of online learning platforms. However, no equivalent assistance exists for physical chess games, creating a divide between analog and digital chess experiences. This paper presents CVChess, a deep learning framework for converting chessboard images to Forsyth-Edwards Notation (FEN), which is later input into online chess engines to provide you with the best next move. Our approach employs a convolutional neural network (CNN) with residual layers to perform piece recognition from smartphone camera images. The system processes RGB images of a physical chess board through a multistep process: image preprocessing using the Hough Line Transform for edge detection, projective transform to achieve a top-down board alignment, segmentation into 64 individual squares, and piece classification into 13 classes (6 unique white pieces, 6 unique black pieces and an empty square) using the residual CNN. Residual connections help retain low-level visual features while enabling deeper feature extraction, improving accuracy and stability during training. We train and evaluate our model using the Chess Recognition Dataset (ChessReD), containing 10,800 annotated smartphone images captured under diverse lighting conditions and angles. The resulting classifications are encoded as an FEN string, which can be fed into a chess engine to generate the most optimal move

